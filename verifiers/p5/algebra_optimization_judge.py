#!/usr/bin/env python3
"""Exact verifier for finite-field, tournament, facility, and subgroup certificates."""
from __future__ import annotations
import heapq,itertools,json,sys
from collections import Counter,deque
from pathlib import Path

TASKS={"P5FFP21","P5TFV22","P5FAC23","P5SUB24"}
def fail(m):raise ValueError(m)
def deg(a):return a.bit_length()-1
def poly_mod(a,m):
    while a and deg(a)>=deg(m):a^=m<<(deg(a)-deg(m))
    return a
def poly_mul(a,b,m):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if deg(a)>=deg(m):a^=m<<(deg(a)-deg(m))
    return poly_mod(out,m)
def poly_pow(a,e,m,trace=False):
    acc=1; base=a; rows=[]; bit=0
    while e:
        before=acc
        if e&1:acc=poly_mul(acc,base,m)
        rows.append({"bit":bit,"exponent_bit":e&1,"acc_before":before,"base":base,"acc_after_multiply":acc})
        base=poly_mul(base,base,m);rows[-1]["base_after_square"]=base;e>>=1;bit+=1
    return (acc,rows) if trace else acc
def poly_gcd(a,b):
    while b:a,b=b,poly_mod(a,b)
    return a
def factor(n):
    rows=[];d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            rows.append([d,e])
        d+=1 if d==2 else 2
    if n>1:rows.append([n,1])
    return rows
def derive_ffp(inp):
    p,n=inp["prime"],inp["degree"]
    if p!=2 or n<12:fail("implemented backend requires F2 degree>=12")
    modulus=inp["modulus_bits"];x=2;fro=[];current=x
    for k in range(1,n+1):
        current=poly_mul(current,current,modulus);g=poly_gcd(current^x,modulus);fro.append({"k":k,"x_to_2k_mod_f":current,"gcd_with_x":g})
    if current!=x or any(row["gcd_with_x"]!=1 for row in fro[:-1]):fail("modulus reducible")
    order=(1<<n)-1;fac=factor(order);tests=[];g=inp["primitive_element_bits"]
    for q,_ in fac:
        value,trace=poly_pow(g,order//q,modulus,True);tests.append({"prime_divisor":q,"exponent":order//q,"power_trace":trace,"result":value})
        if value==1:fail("element not primitive")
    if len(fac)<5:fail("too few distinct order tests")
    return {"modulus_bits":modulus,"irreducibility_frobenius_trace":fro,"order_factorization":fac,"primitive_element_bits":g,"prime_divisor_order_tests":tests,"exact_order":order}

def tournament_triangles(inp):
    n=inp["vertices"];beats=inp["beats"]
    if len(beats)!=n or any(len(r)!=n for r in beats):fail("bad matrix")
    for i in range(n):
        if beats[i][i] or any(beats[i][j]+beats[j][i]!=1 for j in range(n) if i!=j):fail("not tournament")
    tri=[]
    for a,b,c in itertools.combinations(range(n),3):
        if (beats[a][b] and beats[b][c] and beats[c][a]) or (beats[a][c] and beats[c][b] and beats[b][a]):tri.append((a,b,c))
    return tri
def tfv_search(weights,triangles):
    tri_masks=[sum(1<<v for v in row) for row in triangles]; n=len(weights);best=sum(weights)+1;best_mask=0;nodes=prunes=0;memo={}
    # deterministic greedy incumbent
    mask=0
    while True:
        uncovered=next((t for t in tri_masks if not t&mask),None)
        if uncovered is None:break
        candidates=[v for v in range(n) if uncovered>>v&1];v=min(candidates,key=lambda x:(weights[x],x));mask|=1<<v
    best=sum(weights[v] for v in range(n) if mask>>v&1);best_mask=mask
    def rec(mask,cost):
        nonlocal best,best_mask,nodes,prunes
        nodes+=1
        if cost>=best or memo.get(mask,10**18)<=cost:prunes+=1;return
        memo[mask]=cost
        uncovered_rows=[t for t in tri_masks if not t&mask]
        if not uncovered_rows:best,best_mask=cost,mask;return
        used=0;lower=0
        for t in uncovered_rows:
            if not t&used:
                vertices=[v for v in range(n) if t>>v&1];lower+=min(weights[v] for v in vertices);used|=t
        if cost+lower>=best:prunes+=1;return
        uncovered=uncovered_rows[0]
        for v in sorted((v for v in range(n) if uncovered>>v&1),key=lambda x:(weights[x],x)):
            rec(mask|1<<v,cost+weights[v])
    rec(0,0)
    return best,best_mask,{"nodes":nodes,"cost_prunes":prunes}
def topological_order(inp,deleted):
    remain=[v for v in range(inp["vertices"]) if v not in deleted];beats=inp["beats"]
    # acyclic tournament order is decreasing outdegree within residual
    order=sorted(remain,key=lambda v:(-sum(beats[v][u] for u in remain),v))
    if any(not beats[order[i]][order[j]] for i in range(len(order)) for j in range(i+1,len(order))):fail("residual cyclic")
    return order
def derive_tfv(inp):
    tri=tournament_triangles(inp);opt,mask,trace=tfv_search(inp["weights"],tri);deleted=[v for v in range(inp["vertices"]) if mask>>v&1];order=topological_order(inp,set(deleted))
    return {"directed_triangles":[list(x) for x in tri],"deleted_vertices":deleted,"residual_total_order":order,"exact_weight":opt,"branch_bound_lower_certificate":{**trace,"optimum":opt,"triangle_count":len(tri)}}

def mincost_assignment(opened,capacity,costs):
    clients=len(costs); facilities=len(capacity);source=0;cbase=1;fbase=1+clients;sink=1+clients+facilities;N=sink+1;graph=[[] for _ in range(N)]
    def edge(u,v,cap,cost):graph[u].append([v,cap,cost,len(graph[v])]);graph[v].append([u,0,-cost,len(graph[u])-1])
    for c in range(clients):edge(source,cbase+c,1,0)
    for c in range(clients):
        for f in opened:edge(cbase+c,fbase+f,1,costs[c][f])
    for f in opened:edge(fbase+f,sink,capacity[f],0)
    flow=total=augmentations=0;pot=[0]*N
    while flow<clients:
        dist=[10**18]*N;prev=[None]*N;dist[source]=0;heap=[(0,source)]
        while heap:
            d,u=heapq.heappop(heap)
            if d!=dist[u]:continue
            for i,e in enumerate(graph[u]):
                v,cap,cost,_=e
                if cap and d+cost+pot[u]-pot[v]<dist[v]:dist[v]=d+cost+pot[u]-pot[v];prev[v]=(u,i);heapq.heappush(heap,(dist[v],v))
        if prev[sink] is None:return None
        for v in range(N):
            if dist[v]<10**18:pot[v]+=dist[v]
        v=sink
        while v!=source:
            u,i=prev[v];e=graph[u][i];e[1]-=1;graph[v][e[3]][1]+=1;total+=e[2];v=u
        flow+=1;augmentations+=1
    assignment=[-1]*clients
    for c in range(clients):
        for e in graph[cbase+c]:
            if fbase<=e[0]<fbase+facilities and e[1]==0:assignment[c]=e[0]-fbase;break
    return total,assignment,augmentations
def facility_search(inp):
    m=len(inp["opening_costs"]);clients=len(inp["assignment_costs"]);caps=inp["capacities"];min_open=(sum(inp["demands"])+max(caps)-1)//max(caps);best=10**18;best_data=None;nodes=capacity_prunes=feasible=flow_augmentations=0
    def rec(i,opened,open_cost,total_cap):
        nonlocal best,best_data,nodes,capacity_prunes,feasible,flow_augmentations
        nodes+=1
        if total_cap+sum(caps[i:])<sum(inp["demands"]):capacity_prunes+=1;return
        if open_cost>=best:return
        if i==m:
            if total_cap<sum(inp["demands"]):return
            feasible+=1;res=mincost_assignment(opened,caps,inp["assignment_costs"])
            if res:
                assign_cost,assignment,augmentations=res;flow_augmentations+=augmentations;value=open_cost+assign_cost
                if value<best:best=value;best_data=(opened[:],assignment,assign_cost)
            return
        rec(i+1,opened,open_cost,total_cap)
        opened.append(i);rec(i+1,opened,open_cost+inp["opening_costs"][i],total_cap+caps[i]);opened.pop()
    rec(0,[],0,0)
    return best,best_data,{"nodes":nodes+flow_augmentations,"facility_subset_nodes":nodes,"assignment_augmentation_nodes":flow_augmentations,"capacity_prunes":capacity_prunes,"feasible_open_sets_checked":feasible,"minimum_open_count_bound":min_open}
def derive_fac(inp):
    best,data,trace=facility_search(inp)
    if data is None:fail("no assignment")
    opened,assignment,assign_cost=data;loads=[0]*len(inp["capacities"])
    for c,f in enumerate(assignment):loads[f]+=inp["demands"][c]
    return {"opened_facilities":opened,"client_assignment":assignment,"facility_loads":loads,"opening_cost_total":sum(inp["opening_costs"][f] for f in opened),"assignment_cost_total":assign_cost,"exact_total_cost":best,"cost_capacity_tables":{"opening_costs":inp["opening_costs"],"capacities":inp["capacities"],"demands":inp["demands"],"assignment_costs":inp["assignment_costs"]},"lower_cost_infeasibility_branch_bound":{**trace,"optimum":best,"no_solution_below":best}}

def closure(table,seeds):
    n=len(table);S=set(seeds);checks=0;changed=True
    while changed:
        changed=False;current=sorted(S)
        for a in current:
            for b in current:
                checks+=1;c=table[a][b]
                if c not in S:S.add(c);changed=True
    return frozenset(S),checks
def derive_sub(inp):
    table=inp["multiplication_table"];n=len(table);identity=next((e for e in range(n) if all(table[e][x]==x and table[x][e]==x for x in range(n))),None)
    if identity is None:fail("no identity")
    subs={frozenset({identity}):[]};queue=deque([frozenset({identity})]);trace=[];total_checks=0
    while queue:
        H=queue.popleft();hid=None
        for g in range(n):
            if g in H:continue
            K,checks=closure(table,set(H)|{g});total_checks+=checks;trace.append({"source_bitset":sum(1<<x for x in H),"adjoined_element":g,"closure_bitset":sum(1<<x for x in K),"multiplication_checks":checks})
            if K not in subs:subs[K]=subs[H]+[g];queue.append(K)
    ordered=sorted(subs,key=lambda H:(len(H),sum(1<<x for x in H)));index={H:i for i,H in enumerate(ordered)};covers=[]
    for i,H in enumerate(ordered):
        for j,K in enumerate(ordered):
            if len(H)<len(K) and H<K and not any(H<L<K for L in ordered):covers.append([i,j])
    if len(ordered)<25 or total_checks<10000:fail("subgroup scale gate failed")
    return {"subgroup_bitsets":[sum(1<<x for x in H) for H in ordered],"canonical_generators":[subs[H] for H in ordered],"exhaustive_generator_closure_trace":trace,"completeness_multiplication_checks":total_checks,"hasse_covers":covers,"subgroup_count":len(ordered)}

DERIVERS={"P5FFP21":derive_ffp,"P5TFV22":derive_tfv,"P5FAC23":derive_fac,"P5SUB24":derive_sub}
def main():
    if len(sys.argv)!=3:return 2
    try:
        root=Path(sys.argv[1]);artifact=json.loads(Path(sys.argv[2]).read_text("utf-8"));inp=json.loads((root/"input.json").read_text("utf-8"));task=inp.get("task_id")
        if task not in TASKS or root.name!=task:fail("task mismatch")
        expected=DERIVERS[task](inp)
        if set(artifact)!=set(expected) or artifact!=expected:fail("certificate mismatch")
    except Exception as exc:print(f"REJECT: {exc}");return 1
    print("ACCEPT: exact certificate replayed");return 0
if __name__=="__main__":raise SystemExit(main())
