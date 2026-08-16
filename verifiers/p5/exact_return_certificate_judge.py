#!/usr/bin/env python3
"""Exact standard-library verifier for RS, tridiagonal spectrum, Ising, and heat certificates."""
from __future__ import annotations
import json,math,sys
from decimal import Decimal,getcontext
from fractions import Fraction
from pathlib import Path

TASKS={"P5RS25","P5EIG26","P5ISI27","P5HEA28"}
def fail(message): raise ValueError(message)
def inv(a,p): return pow(a%p,p-2,p)
def poly_eval(a,x,p):
    out=0
    for c in reversed(a):out=(out*x+c)%p
    return out
def poly_mul(a,b,p):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    return out
def rs_generator(alpha,t,p):
    g=[1]
    for j in range(1,2*t+1):g=poly_mul(g,[(-pow(alpha,j,p))%p,1],p)
    return g
def bm(s,p):
    size=len(s);C=[1]+[0]*size;B=[1]+[0]*size;L=0;m=1;b=1;trace=[]
    for N in range(size):
        discrepancy=s[N]
        for i in range(1,L+1):discrepancy=(discrepancy+C[i]*s[N-i])%p
        before=C[:L+1];oldL=L
        if discrepancy==0:m+=1
        else:
            T=C[:];coef=discrepancy*inv(b,p)%p
            for j in range(size+1-m):C[j+m]=(C[j+m]-coef*B[j])%p
            if 2*L<=N:L=N+1-L;B=T;b=discrepancy;m=1
            else:m+=1
        trace.append({"step":N,"syndrome":s[N],"discrepancy":discrepancy,"degree_before":oldL,"locator_before":before,"degree_after":L,"locator_after":C[:L+1]})
    return C[:L+1],trace
def solve_mod(matrix,values,p):
    n=len(values);a=[[x%p for x in row]+[values[i]%p] for i,row in enumerate(matrix)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if a[r][col]),None)
        if pivot is None:fail("singular modular reconstruction")
        a[col],a[pivot]=a[pivot],a[col];scale=inv(a[col][col],p);a[col]=[(x*scale)%p for x in a[col]]
        for r in range(n):
            if r==col:continue
            q=a[r][col]
            if q:a[r]=[(x-q*y)%p for x,y in zip(a[r],a[col])]
    return [a[i][-1] for i in range(n)]
def derive_rs(inp):
    p,n,k,t,alpha=inp["prime"],inp["length"],inp["dimension"],inp["correction_radius"],inp["primitive_element"]
    received=inp["received_word"]
    if n<127 or len(received)!=n or n-k!=2*t:fail("RS scale/schema")
    synd=[sum(received[i]*pow(alpha,i*j,p) for i in range(n))%p for j in range(1,2*t+1)]
    locator,trace=bm(synd,p);degree=len(locator)-1
    chien=[];positions=[]
    for i in range(n):
        z=inv(pow(alpha,i,p),p);value=poly_eval(locator,z,p);chien.append({"position":i,"inverse_location":z,"locator_value":value})
        if value==0:positions.append(i)
    if degree!=len(positions) or degree>t:fail("locator/root count")
    xs=[pow(alpha,i,p) for i in positions]
    values=solve_mod([[pow(x,row+1,p) for x in xs] for row in range(degree)],synd[:degree],p) if degree else []
    corrected=received[:]
    for pos,value in zip(positions,values):corrected[pos]=(corrected[pos]-value)%p
    after=[sum(corrected[i]*pow(alpha,i*j,p) for i in range(n))%p for j in range(1,2*t+1)]
    if any(after):fail("correction did not reach code")
    omega=poly_mul(locator,synd,p)[:2*t]
    return {"corrected_codeword":corrected,"received_syndromes":synd,"error_locator":locator,"error_evaluator":omega,"error_positions":positions,"error_values":values,"berlekamp_massey_trace":trace,"chien_search_table":chien,"corrected_syndromes":after,"error_count":degree}

def sturm_trace(diag,off,x):
    pivots=[];q=Fraction(diag[0])-x;neg=1 if q<0 else 0;pivots.append(q)
    for i in range(1,len(diag)):
        if q==0:fail("endpoint is eigenvalue")
        q=Fraction(diag[i])-x-Fraction(off[i-1]*off[i-1],1)/q;pivots.append(q);neg+=q<0
    return neg,[{"numerator":z.numerator,"denominator":z.denominator,"negative":z<0} for z in pivots]
def inverse_vector(diag,off,mid_num,mid_den,index,bits=50):
    getcontext().prec=100;n=len(diag);mu=Decimal(mid_num)/Decimal(mid_den)+Decimal(1)/(Decimal(2)**80);a=[Decimal(x) for x in off];d=[Decimal(x)-mu for x in diag]
    x=[Decimal(0)]*n;x[index]=Decimal(1)
    for _ in range(12):
        cp=[Decimal(0)]*(n-1);dp=[Decimal(0)]*n;den=d[0];cp[0]=a[0]/den;dp[0]=x[0]/den
        for i in range(1,n):
            den=d[i]-a[i-1]*cp[i-1]
            if i<n-1:cp[i]=a[i]/den
            dp[i]=(x[i]-a[i-1]*dp[i-1])/den
        y=[Decimal(0)]*n;y[-1]=dp[-1]
        for i in range(n-2,-1,-1):y[i]=dp[i]-cp[i]*y[i+1]
        scale=max(abs(z) for z in y);x=[z/scale for z in y]
    vden=1<<bits;return [int((z*Decimal(vden)).to_integral_value()) for z in x],vden
def derive_eig(inp):
    diag,off=inp["diagonal"],inp["off_diagonal"];n=len(diag)
    if n<96 or len(off)!=n-1 or any(x==0 for x in off):fail("EIG scale/irreducible coupling")
    q=inp["interval_bits"];den=1<<q;lower=min(diag[i]-(abs(off[i-1]) if i else 0)-(abs(off[i]) if i+1<n else 0) for i in range(n))-1;upper=max(diag[i]+(abs(off[i-1]) if i else 0)+(abs(off[i]) if i+1<n else 0) for i in range(n))+1;rows=[]
    for index in range(n):
        lo=lower*den;hi=upper*den
        while hi-lo>1:
            mid=(lo+hi)//2;count,_=sturm_trace(diag,off,Fraction(mid,den))
            if count<=index:lo=mid
            else:hi=mid
        lc,lt=sturm_trace(diag,off,Fraction(lo,den));uc,ut=sturm_trace(diag,off,Fraction(hi,den))
        if lc!=index or uc!=index+1:fail("interval count isolation")
        mid_num=lo+hi;mid_den=2*den;vec,vden=inverse_vector(diag,off,mid_num,mid_den,index);residual=[]
        for i in range(n):
            z=(diag[i]*mid_den-mid_num)*vec[i]
            if i:z+=off[i-1]*mid_den*vec[i-1]
            if i+1<n:z+=off[i]*mid_den*vec[i+1]
            residual.append(z)
        rmax=max(abs(z) for z in residual);vmax=max(abs(z) for z in vec)
        if rmax*100000>=mid_den*vmax:fail("eigenvector residual too large")
        rows.append({"index":index,"lower_numerator":lo,"upper_numerator":hi,"interval_denominator":den,"lower_sturm_count":lc,"upper_sturm_count":uc,"lower_ldl_trace":lt,"upper_ldl_trace":ut,"midpoint_numerator":mid_num,"midpoint_denominator":mid_den,"eigenvector_numerators":vec,"eigenvector_denominator":vden,"residual_numerators":residual,"residual_denominator":mid_den*vden,"residual_linf_numerator":rmax})
    gaps=[rows[i+1]["lower_numerator"]-rows[i]["upper_numerator"] for i in range(n-1)]
    return {"dimension":n,"irreducible_offdiagonal_nonzero":all(off),"dyadic_eigenpairs":rows,"all_endpoint_count_trace_complete":True,"minimum_interval_gap_numerator":min(gaps),"common_interval_denominator":den,"close_pair_indices":[46,47]}

def vertical_weights(width,same_rows,diff_rows,field_zero,field_one,periodic=True):
    out=[]
    for state in range(1<<width):
        w=1;limit=width if periodic else width-1
        for i in range(width):w*=field_one[i] if (state>>i)&1 else field_zero[i]
        for i in range(limit):w*=same_rows[i] if ((state>>i)&1)==((state>>((i+1)%width))&1) else diff_rows[i]
        out.append(w)
    return out
def isi_vectors(inp,periodic=None):
    width,length=inp["width"],inp["length"]
    if width<10 or length<40:fail("ISI scale")
    periodic=inp["periodic_vertical"] if periodic is None else periodic;vertical=[]
    for col in range(length):vertical.append(vertical_weights(width,inp["vertical_same_weights"][col],inp["vertical_different_weights"][col],inp["field_zero_weights"][col],inp["field_one_weights"][col],periodic))
    vectors=[vertical[0][:]]
    for col in range(1,length):
        vec=vectors[-1][:]
        for bit in range(width):
            step=1<<bit;same=inp["horizontal_same_weights"][col][bit];diff=inp["horizontal_different_weights"][col][bit]
            for base in range(0,1<<width,step*2):
                for j in range(step):
                    i0=base+j;i1=i0+step;a,b=vec[i0],vec[i1];vec[i0]=same*a+diff*b;vec[i1]=diff*a+same*b
        vec=[vec[s]*vertical[col][s] for s in range(1<<width)];vectors.append(vec)
    return vertical,vectors
def derive_isi(inp):
    vertical,vectors=isi_vectors(inp);mask=(1<<inp["width"])-1;checks=[]
    for col,v in enumerate(vectors):checks.append({"column":col,"complement_difference_l1":sum(abs(v[s]-v[s^mask]) for s in range(len(v))),"column_sum":sum(v),"nonzero_state_count":sum(x!=0 for x in v)})
    return {"periodic_boundary_contributions":vertical,"transfer_vectors":vectors,"symmetry_checks":checks,"final_partition_value":sum(vectors[-1]),"width":inp["width"],"length":inp["length"]}

def heat_boundary(inp,i,j):
    n=inp["interior_size"]
    if i==0:return inp["boundary"]["top"][j]
    if i==n+1:return inp["boundary"]["bottom"][j]
    if j==0:return inp["boundary"]["left"][i]
    if j==n+1:return inp["boundary"]["right"][i]
    fail("not boundary")
def validate_heat(inp,a):
    required={"field_numerators","field_denominator","stencil_residual_numerators","stencil_residual_denominator","boundary_values","boundary_contribution_table","m_matrix_margin","energy_lhs_numerator","energy_rhs_numerator","energy_denominator","exact_error_bound_numerator"}
    if set(a)!=required:fail("heat schema")
    n=inp["interior_size"];den=a["field_denominator"];field=a["field_numerators"]
    if n<32 or den<=0 or len(field)!=n or any(len(r)!=n for r in field):fail("heat scale/field")
    if a["boundary_values"]!=inp["boundary"]:fail("boundary mismatch")
    r=inp["reaction"];res=[];bc=[];lhs=rhs=0
    for i in range(1,n+1):
        rr=[];bb=[]
        for j in range(1,n+1):
            u=field[i-1][j-1];neighbor_interior=0;bcon=0
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 1<=x<=n and 1<=y<=n:neighbor_interior+=field[x-1][y-1]
                else:bcon+=heat_boundary(inp,x,y)*den
            effective=inp["source"][i-1][j-1]*den+bcon
            z=(4+r)*u-neighbor_interior-effective;rr.append(z);bb.append(bcon//den);lhs+=u*((4+r)*u-neighbor_interior);rhs+=u*effective
        res.append(rr);bc.append(bb)
    if any(any(row) for row in res):fail("nonzero stencil residual")
    expected={"field_numerators":field,"field_denominator":den,"stencil_residual_numerators":res,"stencil_residual_denominator":den,"boundary_values":inp["boundary"],"boundary_contribution_table":bc,"m_matrix_margin":r,"energy_lhs_numerator":lhs,"energy_rhs_numerator":rhs,"energy_denominator":den*den,"exact_error_bound_numerator":0}
    if a!=expected:fail("heat certificate mismatch")

DERIVERS={"P5RS25":derive_rs,"P5EIG26":derive_eig,"P5ISI27":derive_isi}
def main():
    if len(sys.argv)!=3:return 2
    try:
        root=Path(sys.argv[1]);a=json.loads(Path(sys.argv[2]).read_text("utf-8"));inp=json.loads((root/"input.json").read_text("utf-8"));task=inp.get("task_id")
        if task not in TASKS or root.name!=task:fail("task mismatch")
        if task=="P5HEA28":validate_heat(inp,a)
        elif a!=DERIVERS[task](inp):fail("certificate mismatch")
    except Exception as exc:print(f"REJECT: {exc}");return 1
    print("ACCEPT: exact certificate replayed");return 0
if __name__=="__main__":raise SystemExit(main())
