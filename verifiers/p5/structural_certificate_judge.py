#!/usr/bin/env python3
"""Standard-library structural certificate verifier for P5 batch 02a."""

from __future__ import annotations

import itertools
import json
import sys
from collections import deque
from pathlib import Path


TASKS = {"P5ROT11", "P5CAY12", "P5BRN13", "P5DES14", "P5HAM15"}


def fail(message: str) -> None:
    raise ValueError(message)


def exact_keys(value: dict, expected: set[str], where: str) -> None:
    if not isinstance(value, dict) or set(value) != expected:
        fail(f"{where}: exact keys required: {sorted(expected)}")


def perm_compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(p)
    for i, value in enumerate(p):
        result[value] = i
    return tuple(result)


def group_closure(generators: list[list[int]], degree: int) -> list[tuple[int, ...]]:
    identity = tuple(range(degree))
    gens = [tuple(g) for g in generators]
    if any(sorted(g) != list(identity) for g in gens):
        fail("generator is not a permutation")
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in gens:
            nxt = perm_compose(generator, current)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(seen)


def canonical_cycle(items: list[int]) -> list[int]:
    if not items:
        return []
    start = min(range(len(items)), key=lambda i: items[i:]+items[:i])
    return items[start:] + items[:start]


def derive_rot(inp: dict) -> dict:
    vertices = int(inp["vertices"])
    edges = [tuple(edge) for edge in inp["edges"]]
    if any(not (0 <= u < v < vertices) for u, v in edges) or len(set(edges)) != len(edges):
        fail("edges must be unique ordered pairs")
    dart_tail, dart_head, involution = [], [], []
    dart_of: dict[tuple[int, int], int] = {}
    for i, (u, v) in enumerate(edges):
        dart_of[u, v], dart_of[v, u] = 2*i, 2*i+1
        dart_tail.extend([u, v])
        dart_head.extend([v, u])
        involution.extend([2*i+1, 2*i])
    rotations: list[list[int]] = []
    sigma = [-1] * len(involution)
    for v in range(vertices):
        neighbors = inp["rotation_neighbors"][str(v)]
        incident = sorted(dart_head[d] for d in range(len(involution)) if dart_tail[d] == v)
        if sorted(neighbors) != incident:
            fail("rotation does not list every incident dart")
        darts = [dart_of[v, w] for w in neighbors]
        rotations.append(darts)
        for i, dart in enumerate(darts):
            sigma[dart] = darts[(i+1) % len(darts)]
    phi = [sigma[involution[d]] for d in range(len(involution))]
    unseen, faces = set(range(len(phi))), []
    while unseen:
        start = min(unseen)
        orbit, current = [], start
        while current not in orbit:
            orbit.append(current)
            unseen.discard(current)
            current = phi[current]
        if current != start:
            fail("face permutation orbit failed to close")
        faces.append(canonical_cycle(orbit))
    faces.sort()
    chi = vertices - len(edges) + len(faces)
    if (2-chi) % 2:
        fail("rotation system has nonintegral orientable genus")
    return {
        "dart_tail": dart_tail,
        "dart_head": dart_head,
        "dart_involution": involution,
        "vertex_rotations": rotations,
        "face_orbits": faces,
        "euler": {"vertices": vertices, "edges": len(edges), "faces": len(faces), "chi": chi, "orientable_genus": (2-chi)//2},
    }


def derive_cay(inp: dict) -> dict:
    table = inp["multiplication_table"]
    n = len(table)
    if any(len(row) != n or any(not isinstance(x, int) or not 0 <= x < n for x in row) for row in table):
        fail("invalid multiplication table")
    identities = [e for e in range(n) if all(table[e][x] == x and table[x][e] == x for x in range(n))]
    if len(identities) != 1:
        fail("table has no unique identity")
    identity = identities[0]
    inverses = []
    for x in range(n):
        candidates = [y for y in range(n) if table[x][y] == identity and table[y][x] == identity]
        if len(candidates) != 1:
            fail("inverse failure")
        inverses.append(candidates[0])
    assoc = 0
    for a, b, c in itertools.product(range(n), repeat=3):
        if table[table[a][b]][c] != table[a][table[b][c]]:
            fail("associativity failure")
        assoc += 1
    generators = inp["generators"]
    adjacency = [sorted({table[x][g] for g in generators}) for x in range(n)]
    distances = [-1] * n
    parents = [-1] * n
    parent_generators = [-1] * n
    distances[identity], parents[identity] = 0, identity
    queue = deque([identity])
    while queue:
        x = queue.popleft()
        for g in generators:
            y = table[x][g]
            if distances[y] < 0:
                distances[y] = distances[x] + 1
                parents[y], parent_generators[y] = x, g
                queue.append(y)
    if -1 in distances:
        fail("generators do not span the group")
    diameter = max(distances)
    layers = [[x for x, distance in enumerate(distances) if distance == d] for d in range(diameter+1)]
    return {
        "group_law": {"identity": identity, "inverses": inverses, "associativity_checks": assoc},
        "cayley_adjacency": adjacency,
        "bfs": {"distances": distances, "parents": parents, "parent_generators": parent_generators, "layers": layers},
        "diameter": diameter,
        "diameter_witness": min(x for x in range(n) if distances[x] == diameter),
    }


def permutation_cycles(perm: tuple[int, ...]) -> list[list[int]]:
    unseen, cycles = set(range(len(perm))), []
    while unseen:
        start = min(unseen)
        cycle, current = [], start
        while current not in cycle:
            cycle.append(current)
            unseen.discard(current)
            current = perm[current]
        cycles.append(cycle)
    return cycles


def fixed_histogram_dp(perm: tuple[int, ...], colors: int, target: list[int]) -> tuple[list[int], list[list[dict]], int]:
    lengths = sorted(len(cycle) for cycle in permutation_cycles(perm))
    zero = (0,) * colors
    current = {zero: 1}
    layers = [[{"counts": list(zero), "ways": 1}]]
    for length in lengths:
        nxt: dict[tuple[int, ...], int] = {}
        for counts, ways in current.items():
            for color in range(colors):
                new = list(counts)
                new[color] += length
                if new[color] <= target[color]:
                    key = tuple(new)
                    nxt[key] = nxt.get(key, 0) + ways
        current = nxt
        layers.append([{"counts": list(counts), "ways": ways} for counts, ways in sorted(current.items())])
    return lengths, layers, current.get(tuple(target), 0)


def derive_brn(inp: dict) -> dict:
    degree = inp["positions"]
    group = group_closure(inp["generators"], degree)
    remaining = set(group)
    classes: list[list[tuple[int, ...]]] = []
    while remaining:
        representative = min(remaining)
        conjugates = {perm_compose(perm_compose(g, representative), perm_inverse(g)) for g in group}
        klass = sorted(conjugates)
        remaining -= conjugates
        classes.append(klass)
    classes.sort(key=lambda klass: klass[0])
    rows = []
    for klass in classes:
        representative = klass[0]
        lengths, layers, fixed_count = fixed_histogram_dp(representative, inp["colors"], inp["histogram"])
        rows.append({"representative": list(representative), "members": [list(p) for p in klass], "class_size": len(klass), "cycle_lengths": lengths, "fixed_dp_layers": layers, "fixed_count": fixed_count})
    weighted = sum(row["class_size"] * row["fixed_count"] for row in rows)
    if weighted % len(group):
        fail("Burnside sum not divisible")
    identity = tuple(range(degree))
    _, identity_layers, valid_count = fixed_histogram_dp(identity, inp["colors"], inp["histogram"])
    return {"group_elements": [list(p) for p in group], "conjugacy_classes": rows, "identity_histogram_dp_layers": identity_layers, "valid_coloring_count": valid_count, "burnside_weighted_sum": weighted, "orbit_total": weighted//len(group)}


def image_block(block: tuple[int, ...], perm: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(perm[x] for x in block))


def derive_des(inp: dict) -> dict:
    v = inp["v"]
    blocks = [tuple(block) for block in inp["blocks"]]
    if any(len(block) != inp["k"] or len(set(block)) != inp["k"] for block in blocks):
        fail("invalid blocks")
    if len(set(blocks)) != len(blocks):
        fail("duplicate blocks")
    block_index = {block: i for i, block in enumerate(blocks)}
    group = group_closure(inp["generators"], v)
    generator_maps = []
    for generator in map(tuple, inp["generators"]):
        images = [block_index.get(image_block(block, generator), -1) for block in blocks]
        if -1 in images:
            fail("generator does not preserve blocks")
        generator_maps.append(images)
    pair_rows = []
    for a in range(v):
        for b in range(a+1, v):
            indices = [i for i, block in enumerate(blocks) if a in block and b in block]
            pair_rows.append({"pair": [a, b], "incident_blocks": indices, "sum": len(indices)})
    unseen, orbits = set(range(len(blocks))), []
    while unseen:
        rep = min(unseen)
        orbit = sorted({block_index[image_block(blocks[rep], g)] for g in group})
        stabilizer = [i for i, g in enumerate(group) if image_block(blocks[rep], g) == blocks[rep]]
        unseen -= set(orbit)
        orbits.append({"representative_block": rep, "block_indices": orbit, "orbit_size": len(orbit), "stabilizer_group_indices": stabilizer, "stabilizer_size": len(stabilizer), "orbit_stabilizer_product": len(orbit)*len(stabilizer)})
    return {
        "parameters": {"v": v, "b": len(blocks), "k": inp["k"], "lambda": inp["lambda"]},
        "pb_pair_equations": pair_rows,
        "group_elements": [list(g) for g in group],
        "generator_block_maps": generator_maps,
        "block_orbits": orbits,
    }


def graph_properties(n: int, edges: list[tuple[int, int]]) -> dict:
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v); adjacency[v].add(u)
    def connected_without(skip: int | None) -> bool:
        start = next((x for x in range(n) if x != skip), None)
        if start is None:
            return True
        seen, queue = {start}, deque([start])
        while queue:
            x = queue.popleft()
            for y in adjacency[x]:
                if y != skip and y not in seen:
                    seen.add(y); queue.append(y)
        return len(seen) == n-(skip is not None)
    return {"degrees": [len(row) for row in adjacency], "connected": connected_without(None), "connected_after_deleting_each_vertex": [connected_without(v) for v in range(n)]}


def derive_ham(inp: dict) -> dict:
    n = inp["vertices"]
    edges = sorted(tuple(edge) for edge in inp["edges"])
    edge_set = {tuple(sorted(edge)) for edge in edges}
    adjacency = [[v for v in range(n) if v != u and tuple(sorted((u, v))) in edge_set] for u in range(n)]
    props = graph_properties(n, edges)
    if not props["connected"] or min(props["degrees"]) < 2 or not all(props["connected_after_deleting_each_vertex"]):
        fail("graph is not 2-connected with minimum degree two")
    directed = sorted((u, v) for u in range(n) for v in adjacency[u])
    var = {edge: i+1 for i, edge in enumerate(directed)}
    degree_clauses, degree_kinds = [], []
    for u in range(n):
        outgoing = [var[u, v] for v in adjacency[u]]
        degree_clauses.append(outgoing); degree_kinds.append("out_at_least_one")
        for a, b in itertools.combinations(outgoing, 2):
            degree_clauses.append([-a, -b]); degree_kinds.append("out_at_most_one")
    for v in range(n):
        incoming = [var[u, v] for u in range(n) if (u, v) in var]
        degree_clauses.append(incoming); degree_kinds.append("in_at_least_one")
        for a, b in itertools.combinations(incoming, 2):
            degree_clauses.append([-a, -b]); degree_kinds.append("in_at_most_one")
    full = (1 << n)-1
    subtour_masks = list(range(1, full, 2))
    for mask in subtour_masks:
        if not any((mask >> u)&1 and not ((mask >> v)&1) for u, v in directed):
            fail("empty outgoing subtour cut")
    kind_counts = {kind: degree_kinds.count(kind) for kind in sorted(set(degree_kinds))}
    kind_counts["subtour_outgoing_cut"] = len(subtour_masks)
    adjacency_bits = [sum(1 << v for v in row) for row in adjacency]
    reachable = [0] * (1 << (n-1))
    reachable[0] = 1
    for mask in range(1, 1 << n, 2):
        index = mask >> 1
        if mask != 1:
            endpoints = 0
            for end in range(1, n):
                if not ((mask >> end) & 1):
                    continue
                previous = mask ^ (1 << end)
                if reachable[previous >> 1] & adjacency_bits[end]:
                    endpoints |= 1 << end
            reachable[index] = endpoints
    closing_bits = reachable[full >> 1] & adjacency_bits[0]
    return {
        "graph_checks": props,
        "successor_variables": [{"id": var[edge], "tail": edge[0], "head": edge[1]} for edge in directed],
        "successor_cnf": {"degree_clauses": degree_clauses, "degree_clause_kinds": degree_kinds, "subtour_anchor_masks": subtour_masks, "kind_counts": kind_counts},
        "source_bridge": {"encoding": "directed exactly-one successor/predecessor plus outgoing cut for every odd proper mask (anchor 0 contained)", "anchor": 0, "variable_count": len(var), "degree_clause_count": len(degree_clauses), "subtour_clause_count": len(subtour_masks), "total_clause_count": len(degree_clauses)+len(subtour_masks)},
        "held_karp_infeasibility": {"reachable_endpoint_bitsets_by_odd_mask_index": reachable, "index_rule": "entry i represents odd mask 2*i+1; endpoint v is reachable iff bit v is set", "full_mask": full, "closing_endpoint_bitset": closing_bits, "hamiltonian_cycle_exists": bool(closing_bits)},
    }


DERIVERS = {"P5ROT11": derive_rot, "P5CAY12": derive_cay, "P5BRN13": derive_brn, "P5DES14": derive_des, "P5HAM15": derive_ham}


def verify(task_root: Path, artifact_path: Path) -> None:
    inp = json.loads((task_root / "input.json").read_text("utf-8"))
    artifact = json.loads(artifact_path.read_text("utf-8"))
    task_id = inp.get("task_id")
    if task_id not in TASKS or task_root.name != task_id:
        fail("task identity mismatch")
    expected = DERIVERS[task_id](inp)
    exact_keys(artifact, set(expected), "artifact")
    if artifact != expected:
        fail("certificate does not equal the canonical independently replayed certificate")
    if task_id == "P5HAM15" and artifact["held_karp_infeasibility"]["hamiltonian_cycle_exists"]:
        fail("graph is Hamiltonian")
    if task_id == "P5DES14" and any(row["sum"] != inp["lambda"] for row in artifact["pb_pair_equations"]):
        fail("pair-count PB equality failed")


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: p5c_certificate_judge.py TASK_ROOT ARTIFACT", file=sys.stderr)
        return 2
    try:
        verify(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
    except Exception as exc:
        print(f"REJECT: {exc}")
        return 1
    print("ACCEPT: exact structural certificate replayed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
