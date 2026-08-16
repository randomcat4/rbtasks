#!/usr/bin/env python3
"""Exact exhaustive-certificate verifier for P5 batch 02b."""

from __future__ import annotations

import itertools
import json
import sys
from collections import Counter
from pathlib import Path


TASKS = {"P5LAT16", "P5STS17", "P5CAP18", "P5BIN19", "P5QAS20"}


def fail(message: str) -> None:
    raise ValueError(message)


def exact(artifact: dict, expected: dict) -> None:
    if not isinstance(artifact, dict) or set(artifact) != set(expected):
        fail("exact top-level schema required")
    if artifact != expected:
        fail("artifact differs from canonical independently replayed certificate")


def latin_search(grid: list[list[int]], block: tuple[tuple[int, int, int], ...] | None = None, limit: int | None = None):
    n = len(grid)
    work = [row[:] for row in grid]
    row_used = [set(x for x in row if x >= 0) for row in work]
    col_used = [set(work[r][c] for r in range(n) if work[r][c] >= 0) for c in range(n)]
    if any(len(row_used[r]) != sum(x >= 0 for x in work[r]) for r in range(n)):
        fail("duplicate clue in row")
    if any(len(col_used[c]) != sum(work[r][c] >= 0 for r in range(n)) for c in range(n)):
        fail("duplicate clue in column")
    blocked = {(r, c): value for r, c, value in (block or ())}
    solutions, nodes, dead = [], 0, 0
    widths = Counter()

    def rec() -> None:
        nonlocal nodes, dead
        if limit is not None and len(solutions) >= limit:
            return
        nodes += 1
        choice = None
        candidates = None
        for r in range(n):
            for c in range(n):
                if work[r][c] >= 0:
                    continue
                opts = [x for x in range(n) if x not in row_used[r] and x not in col_used[c]]
                if choice is None or len(opts) < len(candidates) or (len(opts) == len(candidates) and (r, c) < choice):
                    choice, candidates = (r, c), opts
        if choice is None:
            if blocked and all(work[r][c] == value for (r, c), value in blocked.items()):
                dead += 1
                return
            solutions.append([row[:] for row in work])
            return
        widths[len(candidates)] += 1
        if not candidates:
            dead += 1
            return
        r, c = choice
        for value in candidates:
            work[r][c] = value; row_used[r].add(value); col_used[c].add(value)
            rec()
            row_used[r].remove(value); col_used[c].remove(value); work[r][c] = -1

    rec()
    return solutions, {"nodes": nodes, "dead_ends": dead, "branch_width_histogram": [[k, widths[k]] for k in sorted(widths)], "solution_count": len(solutions)}


def derive_lat(inp: dict) -> dict:
    grid = inp["partial_square"]
    n = len(grid)
    empty = [[r, c] for r in range(n) for c in range(n) if grid[r][c] < 0]
    solutions, search = latin_search(grid)
    if len(solutions) != 1:
        fail("partial Latin square not uniquely completable")
    completion = solutions[0]
    block = tuple((r, c, completion[r][c]) for r, c in empty)
    blocked_solutions, blocked_search = latin_search(grid, block)
    if blocked_solutions:
        fail("blocking clause does not prove uniqueness")
    cell_clauses = n*n*(1+n*(n-1)//2)
    row_clauses = n*n*(1+n*(n-1)//2)
    col_clauses = row_clauses
    clues = n*n-len(empty)
    blocking = [-((r*n+c)*n+completion[r][c]+1) for r, c in empty]
    return {
        "completion": completion,
        "originally_empty_cells": empty,
        "exact_cnf_bridge": {"variable_rule": "var(r,c,s)=((r*n+c)*n+s)+1", "variable_count": n**3, "cell_clause_count": cell_clauses, "row_symbol_clause_count": row_clauses, "column_symbol_clause_count": col_clauses, "clue_unit_count": clues, "blocking_clause": blocking, "total_clause_count_with_block": cell_clauses+row_clauses+col_clauses+clues+1},
        "completion_search": search,
        "blocked_second_solution_search": blocked_search,
    }


def pairs_of(triple: tuple[int, int, int]):
    return tuple(itertools.combinations(triple, 2))


def sts_search(v: int, fixed: list[tuple[int, int, int]], candidate: list[tuple[int, int, int]], block_ids: set[int] | None = None, limit: int | None = None):
    fixed_pairs = {pair for triple in fixed for pair in pairs_of(triple)}
    remaining = {pair for pair in itertools.combinations(range(v), 2) if pair not in fixed_pairs}
    incidence = {pair: [] for pair in remaining}
    for i, triple in enumerate(candidate):
        for pair in pairs_of(triple):
            if pair in incidence:
                incidence[pair].append(i)
    chosen, solutions, nodes, dead = [], [], 0, 0
    widths = Counter()

    def rec(uncovered: set[tuple[int, int]]) -> None:
        nonlocal nodes, dead
        if limit is not None and len(solutions) >= limit:
            return
        nodes += 1
        if not uncovered:
            if block_ids is None or set(chosen) != block_ids:
                solutions.append(chosen[:])
            else:
                dead += 1
            return
        pair = min(uncovered, key=lambda p: (sum(all(q in uncovered for q in pairs_of(candidate[i])) for i in incidence[p]), p))
        options = [i for i in incidence[pair] if all(q in uncovered for q in pairs_of(candidate[i]))]
        widths[len(options)] += 1
        if not options:
            dead += 1
        for i in options:
            chosen.append(i); rec(uncovered-set(pairs_of(candidate[i]))); chosen.pop()

    rec(remaining)
    return solutions, incidence, {"nodes": nodes, "dead_ends": dead, "branch_width_histogram": [[k, widths[k]] for k in sorted(widths)], "solution_count": len(solutions)}


def derive_sts(inp: dict) -> dict:
    v = inp["v"]
    fixed = [tuple(row) for row in inp["fixed_blocks"]]
    fixed_pairs = [pair for triple in fixed for pair in pairs_of(triple)]
    if len(set(fixed_pairs)) != len(fixed_pairs):
        fail("fixed blocks reuse a pair")
    candidates = [triple for triple in itertools.combinations(range(v), 3) if all(pair not in set(fixed_pairs) for pair in pairs_of(triple))]
    solutions, incidence, search = sts_search(v, fixed, candidates)
    if len(solutions) != 1:
        fail("partial STS not uniquely completable")
    selected = solutions[0]
    blocked, _, blocked_search = sts_search(v, fixed, candidates, set(selected))
    if blocked:
        fail("blocked STS has another completion")
    remaining_pairs = sorted(incidence)
    pair_rows = [{"pair": list(pair), "candidate_ids": incidence[pair]} for pair in remaining_pairs]
    return {
        "candidate_triples": [list(row) for row in candidates],
        "remaining_pair_incidence": pair_rows,
        "selected_candidate_ids": selected,
        "completion_blocks": [list(row) for row in sorted(fixed+[candidates[i] for i in selected])],
        "exact_cover_cnf_bridge": {"variable_count": len(candidates), "pair_exactly_one_rows": len(remaining_pairs), "blocking_clause": [-(i+1) for i in selected]},
        "completion_search": search,
        "blocked_second_solution_search": blocked_search,
    }


def ternary_vectors(d: int):
    return list(itertools.product(range(3), repeat=d))


def affine_lines(d: int):
    vectors = ternary_vectors(d)
    index = {v: i for i, v in enumerate(vectors)}
    lines = set()
    for a, b in itertools.combinations(vectors, 2):
        c = tuple((-a[i]-b[i]) % 3 for i in range(d))
        if c != a and c != b:
            lines.add(tuple(sorted((index[a], index[b], index[c]))))
    return vectors, sorted(lines)


def cap_max_search(point_count: int, lines: list[tuple[int, int, int]]):
    third = {}
    for a, b, c in lines:
        third[a, b] = c; third[a, c] = b; third[b, c] = a
    best, best_set, nodes, prunes = 0, [], 0, 0
    selected: list[int] = []

    def rec(candidates: list[int]) -> None:
        nonlocal best, best_set, nodes, prunes
        nodes += 1
        if len(selected)+len(candidates) <= best:
            prunes += 1; return
        if not candidates:
            if len(selected) > best:
                best, best_set = len(selected), selected[:]
            return
        v = candidates[-1]
        rest = candidates[:-1]
        forbidden = {third.get(tuple(sorted((u, v)))) for u in selected}
        selected.append(v)
        rec([x for x in rest if x not in forbidden])
        selected.pop()
        rec(rest)

    rec(list(range(point_count)))
    return best, best_set, {"nodes": nodes, "bound_prunes": prunes}


def derive_cap(inp: dict) -> dict:
    d = inp["dimension"]
    vectors, lines = affine_lines(d)
    best, witness, search = cap_max_search(len(vectors), lines)
    if best != inp["claimed_optimum"]:
        fail("claimed cap optimum mismatch")
    line_rows = [{"points": list(line)} for line in lines]
    return {"cap_point_ids": witness, "cap_vectors": [list(vectors[i]) for i in witness], "affine_line_constraints": line_rows, "source_to_constraint_bridge": {"point_count": len(vectors), "line_count": len(lines), "normalization": "sorted point-id triple with coordinate sum zero mod 3"}, "branch_bound_optimality": {**search, "maximum": best, "no_cap_of_size": best+1}}


def contract_bin_instance(inp: dict):
    n = len(inp["weights"])
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a, b in inp["same_bin"]:
        ra, rb = find(a), find(b)
        parent[rb] = ra
    groups = {}
    for i in range(n): groups.setdefault(find(i), []).append(i)
    group_list = sorted(groups.values(), key=lambda g: min(g))
    gid = {x: i for i, group in enumerate(group_list) for x in group}
    conflicts = {tuple(sorted((gid[a], gid[b]))) for a, b in inp["conflicts"]+inp["different_bin"] if gid[a] != gid[b]}
    if any(gid[a] == gid[b] for a, b in inp["conflicts"]+inp["different_bin"]): fail("same group conflicts")
    weights = [sum(inp["weights"][i] for i in group) for group in group_list]
    return group_list, weights, conflicts


def bin_color_search(weights: list[int], conflicts: set[tuple[int, int]], bins: int, capacity: int, stop_first=False):
    n = len(weights)
    neighbors = [set() for _ in range(n)]
    for a, b in conflicts: neighbors[a].add(b); neighbors[b].add(a)
    order = sorted(range(n), key=lambda x: (-len(neighbors[x]), -weights[x], x))
    assignment = [-1]*n; loads = [0]*bins; nodes=dead=0; solutions=[]
    def rec(pos):
        nonlocal nodes, dead
        if stop_first and solutions: return
        nodes += 1
        if pos == n:
            solutions.append(assignment[:]); return
        v = order[pos]; used_empty=False; moved=False
        for color in range(bins):
            if loads[color]+weights[v] > capacity: continue
            if any(assignment[u] == color for u in neighbors[v]): continue
            if loads[color] == 0:
                if used_empty: continue
                used_empty=True
            moved=True; assignment[v]=color; loads[color]+=weights[v]
            rec(pos+1)
            loads[color]-=weights[v]; assignment[v]=-1
        if not moved: dead += 1
    rec(0)
    return solutions, {"nodes": nodes, "dead_ends": dead, "solution_count": len(solutions), "vertex_order": order}


def derive_bin(inp: dict) -> dict:
    groups, weights, conflicts = contract_bin_instance(inp)
    b = inp["claimed_bins"]
    solutions, witness_search = bin_color_search(weights, conflicts, b, inp["capacity"], stop_first=True)
    if not solutions: fail("claimed packing infeasible")
    group_assignment = solutions[0]
    assignment = [0]*len(inp["weights"])
    for g, members in enumerate(groups):
        for item in members: assignment[item] = group_assignment[g]
    lower_solutions, lower_search = bin_color_search(weights, conflicts, b-1, inp["capacity"])
    if lower_solutions: fail("b-1 bins feasible")
    loads = [sum(inp["weights"][i] for i, color in enumerate(assignment) if color == c) for c in range(b)]
    return {"item_to_bin": assignment, "bin_loads": loads, "contracted_groups": groups, "contracted_weights": weights, "contracted_conflicts": [list(row) for row in sorted(conflicts)], "pb_source_bridge": {"capacity": inp["capacity"], "capacity_rows": b, "conflict_rows": len(inp["conflicts"]), "same_rows": len(inp["same_bin"]), "different_rows": len(inp["different_bin"])}, "packing_search": witness_search, "b_minus_one_infeasibility_search": lower_search}


def compose(p, q): return tuple(p[q[i]] for i in range(len(p)))


def derive_qas(inp: dict) -> dict:
    a, b = inp["table_a"], inp["table_b"]
    n = len(a)
    alpha, beta, gamma = inp["isotopy_alpha"], inp["isotopy_beta"], inp["isotopy_gamma"]
    for perm in (alpha, beta, gamma):
        if sorted(perm) != list(range(n)): fail("isotopy map not bijective")
    if any(b[alpha[x]][beta[y]] != gamma[a[x][y]] for x in range(n) for y in range(n)):
        fail("isotopy law failed")
    mapping=[-1]*n; used=set(); nodes=dead=0; depth=Counter(); solutions=[]; failed_prefixes=[]
    def consistent():
        for x in range(n):
            if mapping[x] < 0: continue
            for y in range(n):
                z=a[x][y]
                if mapping[y] >= 0 and mapping[z] >= 0 and b[mapping[x]][mapping[y]] != mapping[z]: return False
        return True
    def rec(pos):
        nonlocal nodes, dead
        nodes+=1; depth[pos]+=1
        if pos==n: solutions.append(mapping[:]); return
        x=pos
        for value in range(n):
            if value in used: continue
            mapping[x]=value; used.add(value)
            if consistent(): rec(pos+1)
            else:
                dead+=1
                if len(failed_prefixes)<200000: failed_prefixes.append(mapping[:pos+1])
            used.remove(value); mapping[x]=-1
    rec(0)
    if solutions: fail("tables are isomorphic")
    return {"isotopy": {"alpha": alpha, "beta": beta, "gamma": gamma}, "isomorphism_cnf_bridge": {"variable_rule": "p(x)=y permutation variables plus operation-preservation clauses", "variable_count": n*n, "row_exactly_one": n, "column_exactly_one": n, "operation_rows": n*n}, "exhaustive_nonisomorphism": {"nodes": nodes, "dead_ends": dead, "nodes_by_depth": [[k, depth[k]] for k in sorted(depth)], "failed_prefixes": failed_prefixes, "solution_count": 0}}


DERIVERS={"P5LAT16":derive_lat,"P5STS17":derive_sts,"P5CAP18":derive_cap,"P5BIN19":derive_bin,"P5QAS20":derive_qas}


def main() -> int:
    if len(sys.argv)!=3: return 2
    try:
        root, artifact_path=Path(sys.argv[1]),Path(sys.argv[2])
        inp=json.loads((root/"input.json").read_text("utf-8")); artifact=json.loads(artifact_path.read_text("utf-8"))
        task=inp.get("task_id")
        if task not in TASKS or root.name!=task: fail("task mismatch")
        exact(artifact,DERIVERS[task](inp))
    except Exception as exc:
        print(f"REJECT: {exc}"); return 1
    print("ACCEPT: exact exhaustive certificate replayed"); return 0


if __name__=="__main__": raise SystemExit(main())
