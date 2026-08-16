#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from collections import deque
from fractions import Fraction
from pathlib import Path

sys.set_int_max_str_digits(0)


class Reject(Exception):
    pass


def need(cond: bool, message: str) -> None:
    if not cond:
        raise Reject(message)


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def rat(value) -> Fraction:
    need(isinstance(value, list) and len(value) == 2, "rational must be [numerator,denominator]")
    n, d = value
    need(isinstance(n, int) and isinstance(d, int) and d > 0, "invalid rational integers")
    need(math.gcd(abs(n), d) == 1, "rational is not reduced")
    return Fraction(n, d)


def canonical_classes(signatures):
    ids = {}
    result = []
    for sig in signatures:
        if sig not in ids:
            ids[sig] = len(ids)
        result.append(ids[sig])
    return result


def check_iso(data, art):
    need(set(art) == {"fit", "blocks", "dual_multipliers", "objective", "dual_objective"}, "ISO top-level schema")
    y = [Fraction(v) for v in data["y"]]
    w = [Fraction(v) for v in data["weights"]]
    n = len(y)
    need(n == 96 and len(w) == n, "frozen ISO dimensions differ")
    fit = [rat(v) for v in art["fit"]]
    need(len(fit) == n, "fit length")
    need(all(fit[i] <= fit[i + 1] for i in range(n - 1)), "fit is not nondecreasing")
    blocks = art["blocks"]
    cursor = 0
    block_means = []
    for block in blocks:
        need(set(block) == {"start", "end", "sum_w", "sum_wy", "mean"}, "block schema")
        start, end = block["start"], block["end"]
        need(start == cursor and isinstance(end, int) and start < end <= n, "block partition")
        sw = sum(w[start:end], Fraction())
        swy = sum((w[i] * y[i] for i in range(start, end)), Fraction())
        mean = swy / sw
        need(rat(block["sum_w"]) == sw and rat(block["sum_wy"]) == swy, "block sums")
        need(rat(block["mean"]) == mean, "block mean")
        need(all(fit[i] == mean for i in range(start, end)), "fit/block mismatch")
        block_means.append(mean)
        cursor = end
    need(cursor == n and blocks, "blocks do not cover input")
    need(all(block_means[i] < block_means[i + 1] for i in range(len(block_means) - 1)), "blocks are not maximal")
    multipliers = [rat(v) for v in art["dual_multipliers"]]
    need(len(multipliers) == n - 1 and all(v >= 0 for v in multipliers), "dual multiplier domain")
    for i in range(n):
        left = multipliers[i - 1] if i else Fraction()
        right = multipliers[i] if i < n - 1 else Fraction()
        need(2 * w[i] * (fit[i] - y[i]) + right - left == 0, f"stationarity at {i}")
        if i < n - 1:
            need(multipliers[i] * (fit[i] - fit[i + 1]) == 0, f"complementarity at {i}")
    objective = sum((w[i] * (fit[i] - y[i]) ** 2 for i in range(n)), Fraction())
    need(rat(art["objective"]) == objective, "objective")
    need(rat(art["dual_objective"]) == objective, "primal/dual objective agreement")


def refinement_rounds(trans, accepting):
    current = canonical_classes([(bool(v),) for v in accepting])
    rounds = [current]
    while True:
        nxt = canonical_classes([(current[s],) + tuple(current[t] for t in trans[s]) for s in range(len(trans))])
        if nxt == current:
            return rounds
        rounds.append(nxt)
        current = nxt


def follow(trans, start, word):
    state = start
    for symbol in word:
        need(isinstance(symbol, int) and 0 <= symbol < len(trans[0]), "symbol out of range")
        state = trans[state][symbol]
    return state


def check_dmn(data, art):
    need(set(art) == {"old_to_quotient", "quotient_transitions", "quotient_accepting", "refinement_rounds", "reachability_parents", "distinguishing_words"}, "DMN top-level schema")
    trans = data["transitions"]
    accepting = data["accepting"]
    start = data["start"]
    n, alphabet = len(trans), len(trans[0])
    need(n == 73 and alphabet == 6 and len(accepting) == n, "frozen DMN dimensions differ")
    need(all(len(row) == alphabet and all(isinstance(t, int) and 0 <= t < n for t in row) for row in trans), "transition domain")
    mapping = art["old_to_quotient"]
    need(len(mapping) == n and all(isinstance(q, int) and q >= 0 for q in mapping), "quotient map")
    qn = max(mapping) + 1
    need(set(mapping) == set(range(qn)), "quotient labels")
    rounds = refinement_rounds(trans, accepting)
    need(art["refinement_rounds"] == rounds, "refinement rounds")
    need(mapping == rounds[-1], "map is not stable Myhill-Nerode partition")
    qtrans = art["quotient_transitions"]
    qaccept = art["quotient_accepting"]
    need(len(qtrans) == qn and len(qaccept) == qn, "quotient dimensions")
    for s in range(n):
        need(bool(qaccept[mapping[s]]) == bool(accepting[s]), "final-state consistency")
        for a in range(alphabet):
            need(qtrans[mapping[s]][a] == mapping[trans[s][a]], "transition homomorphism")
    parents = art["reachability_parents"]
    need(len(parents) == n and parents[start] is None, "reachability root")
    for target in range(n):
        if target == start:
            continue
        seen = set()
        cur = target
        while cur != start:
            need(cur not in seen and len(seen) < n, "cyclic reachability certificate")
            seen.add(cur)
            edge = parents[cur]
            need(isinstance(edge, list) and len(edge) == 2, "missing reachability parent")
            parent, symbol = edge
            need(0 <= parent < n and 0 <= symbol < alphabet and trans[parent][symbol] == cur, "bad reachability edge")
            cur = parent
    words = art["distinguishing_words"]
    need(len(words) == qn * (qn - 1) // 2, "distinguishing pair count")
    expected_pairs = [(p, q) for p in range(qn) for q in range(p + 1, qn)]
    for item, pair in zip(words, expected_pairs):
        need(item["pair"] == list(pair), "distinguishing pair order")
        p, q = pair
        pp, qq = follow(qtrans, p, item["word"]), follow(qtrans, q, item["word"])
        need(bool(qaccept[pp]) != bool(qaccept[qq]), "word does not distinguish pair")


def subset_bfs(trans):
    n = len(trans)
    full = (1 << n) - 1
    masks = [full]
    dist = [0]
    parent = [None]
    symbol = [None]
    index = {full: 0}
    queue = deque([0])
    first_depth = None
    while queue:
        idx = queue.popleft()
        if first_depth is not None and dist[idx] >= first_depth:
            continue
        mask = masks[idx]
        for a in range(len(trans[0])):
            nxt = 0
            bits = mask
            while bits:
                low = bits & -bits
                s = low.bit_length() - 1
                nxt |= 1 << trans[s][a]
                bits -= low
            if nxt not in index:
                index[nxt] = len(masks)
                masks.append(nxt)
                dist.append(dist[idx] + 1)
                parent.append(idx)
                symbol.append(a)
                queue.append(index[nxt])
                if nxt.bit_count() == 1 and first_depth is None:
                    first_depth = dist[-1]
    need(first_depth is not None, "automaton is not synchronizing in reachable search")
    return masks, dist, parent, symbol, first_depth


def check_syn(data, art):
    need(set(art) == {"word", "subset_bfs", "first_singleton_distance"}, "SYN top-level schema")
    trans = data["transitions"]
    need(len(trans) == 48 and len(trans[0]) == 3, "frozen SYN dimensions differ")
    masks, dist, parents, symbols, depth = subset_bfs(trans)
    table = art["subset_bfs"]
    need(len(table) == len(masks), "BFS table is incomplete")
    for i, row in enumerate(table):
        need(row == {"mask": masks[i], "distance": dist[i], "parent": parents[i], "symbol": symbols[i]}, f"BFS row {i}")
    singleton = next(i for i, mask in enumerate(masks) if dist[i] == depth and mask.bit_count() == 1)
    word = []
    cur = singleton
    while parents[cur] is not None:
        word.append(symbols[cur])
        cur = parents[cur]
    word.reverse()
    need(art["word"] == word and len(word) == depth, "shortest synchronizing word")
    need(all(follow(trans, s, word) == follow(trans, 0, word) for s in range(48)), "word does not synchronize all states")
    need(art["first_singleton_distance"] == depth, "first singleton distance")


def parity(value):
    return value.bit_count() & 1


def vit_edge(state, bit, memory, generators):
    combined = (state << 1) | bit
    outputs = [parity(combined & g) for g in generators]
    return combined & ((1 << memory) - 1), outputs


def check_vit(data, art):
    need(set(art) == {"information_bits", "decoded_bits", "state_path", "branch_metrics", "survivor_metrics", "survivor_predecessors", "final_metric"}, "VIT top-level schema")
    received = data["received"]
    memory = data["memory"]
    generators = data["generators"]
    states = 1 << memory
    steps = len(received)
    need(steps == 160 and len(generators) == 2 and states == 16, "frozen VIT dimensions differ")
    branch = art["branch_metrics"]
    need(len(branch) == steps, "branch table length")
    for t in range(steps):
        need(len(branch[t]) == states, "branch state row")
        for s in range(states):
            need(len(branch[t][s]) == 2, "branch bit row")
            for bit in (0, 1):
                _, out = vit_edge(s, bit, memory, generators)
                expected = sum(int(out[j] != received[t][j]) for j in range(2))
                need(branch[t][s][bit] == expected, f"branch metric {t}/{s}/{bit}")
    metrics = art["survivor_metrics"]
    preds = art["survivor_predecessors"]
    need(len(metrics) == steps + 1 and len(preds) == steps + 1, "survivor table length")
    expected_metrics = [[None] * states for _ in range(steps + 1)]
    expected_preds = [[None] * states for _ in range(steps + 1)]
    expected_metrics[0][0] = 0
    for t in range(steps):
        choices = [[] for _ in range(states)]
        for s in range(states):
            if expected_metrics[t][s] is None:
                continue
            for bit in (0, 1):
                nxt, _ = vit_edge(s, bit, memory, generators)
                choices[nxt].append((expected_metrics[t][s] + branch[t][s][bit], s, bit))
        for nxt in range(states):
            if choices[nxt]:
                cost, prev, bit = min(choices[nxt])
                expected_metrics[t + 1][nxt] = cost
                expected_preds[t + 1][nxt] = [prev, bit]
    need(metrics == expected_metrics and preds == expected_preds, "survivor DP or frozen tie-break")
    final_state = data["termination_state"]
    need(art["final_metric"] == metrics[-1][final_state], "final metric")
    bits = []
    path = [final_state]
    cur = final_state
    for t in range(steps, 0, -1):
        edge = preds[t][cur]
        need(edge is not None, "traceback")
        cur, bit = edge
        bits.append(bit)
        path.append(cur)
    bits.reverse()
    path.reverse()
    need(art["decoded_bits"] == bits and art["state_path"] == path, "traceback artifact")
    need(art["information_bits"] == bits[:-memory] and all(v == 0 for v in bits[-memory:]), "termination bits")


def mod_inverse(a, p):
    return pow(a % p, p - 2, p)


def solve_mod(rows, b, p):
    n = len(rows)
    mat = [[0] * (n + 1) for _ in range(n)]
    for i, row in enumerate(rows):
        for j, value in row:
            f = rat(value)
            mat[i][j] = f.numerator * mod_inverse(f.denominator, p) % p
        fb = rat(b[i])
        mat[i][n] = fb.numerator * mod_inverse(fb.denominator, p) % p
    for col in range(n):
        pivot = next((r for r in range(col, n) if mat[r][col]), None)
        need(pivot is not None, f"singular modulo {p}")
        mat[col], mat[pivot] = mat[pivot], mat[col]
        inv = mod_inverse(mat[col][col], p)
        mat[col] = [(v * inv) % p for v in mat[col]]
        for r in range(n):
            if r != col and mat[r][col]:
                factor = mat[r][col]
                mat[r] = [(mat[r][c] - factor * mat[col][c]) % p for c in range(n + 1)]
    return [mat[i][n] for i in range(n)]


def check_lin(data, art):
    need(set(art) == {"x_dyadic", "residual", "dominance_margins", "gamma", "error_bound", "modular_solutions"}, "LIN top-level schema")
    rows, b = data["rows"], data["b"]
    n = len(rows)
    need(n == 180 and len(b) == n, "frozen LIN dimensions differ")
    x = [rat(v) for v in art["x_dyadic"]]
    need(len(x) == n and all(v.denominator & (v.denominator - 1) == 0 for v in x), "dyadic solution")
    residual = []
    margins = []
    for i, row in enumerate(rows):
        seen = set()
        total = Fraction()
        diag = None
        off = Fraction()
        for j, value in row:
            need(isinstance(j, int) and 0 <= j < n and j not in seen, "sparse row index")
            seen.add(j)
            aij = rat(value)
            total += aij * x[j]
            if j == i:
                diag = abs(aij)
            else:
                off += abs(aij)
        need(diag is not None, "missing diagonal")
        margin = diag - off
        need(margin > 0, "input is not strictly row diagonally dominant")
        margins.append(margin)
        residual.append(rat(b[i]) - total)
    need([rat(v) for v in art["residual"]] == residual, "exact residual")
    need([rat(v) for v in art["dominance_margins"]] == margins, "dominance margins")
    gamma = min(margins)
    need(rat(art["gamma"]) == gamma, "minimum dominance margin")
    bound = max(map(abs, residual)) / gamma
    need(rat(art["error_bound"]) == bound, "Varah infinity error bound")
    need(bound <= rat(data["required_error_bound"]), "claimed accuracy threshold")
    expected_indices = data["modular_indices"]
    modular = art["modular_solutions"]
    need([row["prime"] for row in modular] == data["modular_primes"], "modular prime list")
    for row in modular:
        need(row["indices"] == expected_indices, "modular index list")
        solution = solve_mod(rows, b, row["prime"])
        need(row["residues"] == [solution[i] for i in expected_indices], "modular solution residues")


def crt(residues, moduli):
    product = math.prod(moduli)
    value = 0
    for residue, modulus in zip(residues, moduli):
        partial = product // modulus
        value = (value + residue * partial * pow(partial, -1, modulus)) % product
    return value


def check_ksx(data, art):
    need(set(art) == {"statistic", "forbidden", "dp_mod", "crt", "probability"}, "KSX top-level schema")
    sample_a, sample_b = data["sample_a"], data["sample_b"]
    n, m = len(sample_a), len(sample_b)
    need((n, m) == (137, 149) and len(set(sample_a + sample_b)) == n + m, "frozen KSX samples")
    labels = [(v, 0) for v in sample_a] + [(v, 1) for v in sample_b]
    labels.sort()
    i = j = max_diff = 0
    for _, label in labels:
        if label == 0:
            i += 1
        else:
            j += 1
        max_diff = max(max_diff, abs(i * m - j * n))
    statistic = Fraction(max_diff, n * m)
    need(rat(art["statistic"]) == statistic, "KS statistic")
    forbidden = [[abs(i * m - j * n) >= max_diff for j in range(m + 1)] for i in range(n + 1)]
    need(art["forbidden"] == forbidden, "forbidden lattice boundary")
    primes = data["primes"]
    need(all(math.gcd(primes[i], primes[j]) == 1 for i in range(len(primes)) for j in range(i)), "KS CRT moduli are not pairwise coprime")
    need([row["prime"] for row in art["dp_mod"]] == primes, "pinned KS moduli")
    final_residues = []
    for record, prime in zip(art["dp_mod"], primes):
        table = [[0] * (m + 1) for _ in range(n + 1)]
        if not forbidden[0][0]:
            table[0][0] = 1
        for a in range(n + 1):
            for b in range(m + 1):
                if (a == 0 and b == 0) or forbidden[a][b]:
                    continue
                table[a][b] = ((table[a - 1][b] if a else 0) + (table[a][b - 1] if b else 0)) % prime
        need(record["table"] == table, f"KS modular recurrence {prime}")
        final_residues.append(table[n][m])
    total = math.comb(n + m, n)
    product = math.prod(primes)
    need(product > total, "CRT product does not prove unique safe-path reconstruction")
    safe = crt(final_residues, primes)
    tail = total - safe
    crt_art = art["crt"]
    need(crt_art == {"modulus_product": product, "safe_count": safe, "total_paths": total, "tail_count": tail}, "KS CRT reconstruction")
    need(rat(art["probability"]) == Fraction(tail, total), "KS reduced tail probability")


def matrix_mod_residue(value, prime):
    f = rat(value)
    need(f.denominator % prime != 0, f"denominator singular modulo {prime}")
    return f.numerator * pow(f.denominator, -1, prime) % prime


def check_mrk(data, art):
    need(set(art) == {"hitting_times", "absorption_probabilities", "modular_tables", "reconstruction_bounds"}, "MRK top-level schema")
    qrows, rrows = data["Q"], data["R"]
    n, classes = len(qrows), len(rrows[0])
    need(n == 64 and classes == 5 and len(rrows) == n, "frozen MRK dimensions")
    Q = [[Fraction() for _ in range(n)] for _ in range(n)]
    R = [[rat(v) for v in row] for row in rrows]
    for i, row in enumerate(qrows):
        seen = set()
        for j, value in row:
            need(0 <= j < n and j not in seen, "MRK sparse Q index")
            seen.add(j)
            Q[i][j] = rat(value)
        need(all(v >= 0 for v in Q[i]) and all(v >= 0 for v in R[i]), "negative transition probability")
        need(sum(Q[i], Fraction()) + sum(R[i], Fraction()) == 1, "MRK row is not stochastic")
    h = [rat(v) for v in art["hitting_times"]]
    B = [[rat(v) for v in row] for row in art["absorption_probabilities"]]
    need(len(h) == n and len(B) == n and all(len(row) == classes for row in B), "MRK solution dimensions")
    for i in range(n):
        need(h[i] - sum((Q[i][j] * h[j] for j in range(n)), Fraction()) == 1, f"MRK hitting equation {i}")
        for k in range(classes):
            need(B[i][k] - sum((Q[i][j] * B[j][k] for j in range(n)), Fraction()) == R[i][k], f"MRK absorption equation {i}/{k}")
        need(sum(B[i], Fraction()) == 1 and all(v >= 0 for v in B[i]), f"MRK absorption boundary {i}")
    primes = data["primes"]
    tables = art["modular_tables"]
    need([row["prime"] for row in tables] == primes, "MRK pinned primes")
    for record, prime in zip(tables, primes):
        expected_h = [h[i].numerator * pow(h[i].denominator, -1, prime) % prime for i in range(n)]
        expected_B = [[B[i][k].numerator * pow(B[i][k].denominator, -1, prime) % prime for k in range(classes)] for i in range(n)]
        need(record["pivot_product"] % prime != 0, f"MRK singular modular system {prime}")
        need(record["pivot_product"] == 1, "MRK frozen triangular pivot product")
        need(record["hitting_residues"] == expected_h and record["absorption_residues"] == expected_B, f"MRK modular trace {prime}")
        for i in range(n):
            lhs = expected_h[i]
            for j in range(n):
                if Q[i][j]:
                    lhs = (lhs - Q[i][j].numerator * pow(Q[i][j].denominator, -1, prime) * expected_h[j]) % prime
            need(lhs == 1, f"MRK modular hitting equation {prime}/{i}")
    max_num = max(abs(v.numerator) for v in h + [v for row in B for v in row])
    max_den = max(v.denominator for v in h + [v for row in B for v in row])
    bounds = art["reconstruction_bounds"]
    need(bounds == {"max_abs_numerator": max_num, "max_denominator": max_den, "modulus_product": math.prod(primes)}, "MRK reconstruction bounds")
    need(2 * max_num * max_den < math.prod(primes), "MRK rational reconstruction is not unique")


def bit_reverse(value, bits):
    out = 0
    for _ in range(bits):
        out = (out << 1) | (value & 1)
        value >>= 1
    return out


def ntt_trace(values, root, prime, inverse=False):
    n = len(values)
    bits = n.bit_length() - 1
    current = [values[bit_reverse(i, bits)] % prime for i in range(n)]
    stages = [current.copy()]
    length = 2
    use_root = pow(root, -1, prime) if inverse else root
    while length <= n:
        step = pow(use_root, n // length, prime)
        nxt = current.copy()
        for start in range(0, n, length):
            omega = 1
            half = length // 2
            for j in range(half):
                u = current[start + j]
                v = current[start + j + half] * omega % prime
                nxt[start + j] = (u + v) % prime
                nxt[start + j + half] = (u - v) % prime
                omega = omega * step % prime
        current = nxt
        stages.append(current.copy())
        length *= 2
    if inverse:
        inv_n = pow(n, -1, prime)
        current = [v * inv_n % prime for v in current]
        stages.append(current.copy())
    return stages


def check_ntt(data, art):
    need(set(art) == {"padded_length", "coefficient_bound", "prime_traces", "crt_coefficients", "convolution"}, "NTT top-level schema")
    a, b = data["a"], data["b"]
    n = art["padded_length"]
    need((len(a), len(b), n) == (257, 383, 1024), "frozen NTT dimensions")
    bound = min(len(a), len(b)) * max(map(abs, a)) * max(map(abs, b))
    need(art["coefficient_bound"] == bound, "NTT coefficient bound")
    primes = data["primes"]
    need(len(art["prime_traces"]) == 2, "NTT prime trace count")
    inverse_residues = []
    for record, pin in zip(art["prime_traces"], primes):
        prime, generator = pin["prime"], pin["primitive_root"]
        root = pow(generator, (prime - 1) // n, prime)
        need(record["prime"] == prime and record["primitive_root"] == generator and record["root"] == root, "NTT pinned root")
        need(pow(root, n, prime) == 1 and pow(root, n // 2, prime) != 1, "NTT root order")
        padded_a = a + [0] * (n - len(a))
        padded_b = b + [0] * (n - len(b))
        atrace = ntt_trace(padded_a, root, prime)
        btrace = ntt_trace(padded_b, root, prime)
        need(record["forward_a_stages"] == atrace, f"NTT A stages {prime}")
        need(record["forward_b_stages"] == btrace, f"NTT B stages {prime}")
        pointwise = [atrace[-1][i] * btrace[-1][i] % prime for i in range(n)]
        need(record["pointwise"] == pointwise, f"NTT pointwise {prime}")
        itrace = ntt_trace(pointwise, root, prime, inverse=True)
        need(record["inverse_stages"] == itrace, f"NTT inverse stages {prime}")
        inverse_residues.append(itrace[-1])
    product = math.prod(pin["prime"] for pin in primes)
    need(product > 2 * bound, "NTT CRT signed uniqueness bound")
    school = [sum(a[i] * b[k - i] for i in range(max(0, k - len(b) + 1), min(len(a) - 1, k) + 1)) for k in range(len(a) + len(b) - 1)]
    need(art["convolution"] == school, "schoolbook convolution cross-check")
    coeffs = art["crt_coefficients"]
    need(len(coeffs) == len(school), "NTT CRT coefficient count")
    moduli = [pin["prime"] for pin in primes]
    for k, value in enumerate(school):
        residues = [inverse_residues[j][k] for j in range(2)]
        unsigned = crt(residues, moduli)
        signed = unsigned if unsigned <= product // 2 else unsigned - product
        need(coeffs[k] == {"residues": residues, "signed": signed} and signed == value, f"NTT CRT coefficient {k}")


def check_lpc(data, art):
    need(set(art) == {"autocorrelations", "reflection_coefficients", "ar_rows", "prediction_errors", "final_coefficients", "yule_walker_residuals"}, "LPC top-level schema")
    signal, order = data["signal"], data["order"]
    need(len(signal) == 192 and order == 24, "frozen LPC dimensions")
    autocorr = [Fraction(sum(signal[i] * signal[i - lag] for i in range(lag, len(signal)))) for lag in range(order + 1)]
    need([rat(v) for v in art["autocorrelations"]] == autocorr, "LPC autocorrelations")
    errors = [autocorr[0]]
    rows = [[]]
    reflections = []
    for k in range(1, order + 1):
        previous = rows[-1]
        numerator = autocorr[k] + sum((previous[j - 1] * autocorr[k - j] for j in range(1, k)), Fraction())
        need(errors[-1] != 0, f"LPC zero denominator {k}")
        reflection = -numerator / errors[-1]
        row = [previous[j - 1] + reflection * previous[k - j - 1] for j in range(1, k)] + [reflection]
        error = errors[-1] * (1 - reflection * reflection)
        need(error > 0, f"LPC nonpositive prediction error {k}")
        reflections.append(reflection)
        rows.append(row)
        errors.append(error)
    need([rat(v) for v in art["reflection_coefficients"]] == reflections, "LPC reflection trace")
    need([[rat(v) for v in row] for row in art["ar_rows"]] == rows, "LPC intermediate AR rows")
    need([rat(v) for v in art["prediction_errors"]] == errors, "LPC prediction errors")
    need([rat(v) for v in art["final_coefficients"]] == rows[-1], "LPC final coefficients")
    residuals = [autocorr[k] + sum((rows[-1][j - 1] * autocorr[abs(k - j)] for j in range(1, order + 1)), Fraction()) for k in range(1, order + 1)]
    need([rat(v) for v in art["yule_walker_residuals"]] == residuals and all(v == 0 for v in residuals), "LPC Yule-Walker residuals")


def poly_trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_remainder(a, b):
    a, b = poly_trim(a), poly_trim(b)
    while len(a) >= len(b) and any(a):
        factor = a[-1] / b[-1]
        shift = len(a) - len(b)
        for i in range(len(b)):
            a[i + shift] -= factor * b[i]
        a = poly_trim(a)
    return a


def sturm_sequence(poly):
    seq = [poly_trim(poly)]
    derivative = [Fraction(i) * seq[0][i] for i in range(1, len(seq[0]))]
    seq.append(poly_trim(derivative))
    while len(seq[-1]) > 1:
        rem = poly_remainder(seq[-2].copy(), seq[-1])
        rem = [-v for v in rem]
        need(any(rem), "Sturm sequence repeated root")
        seq.append(poly_trim(rem))
    return seq


def sign_at(poly, where):
    if where == "zero":
        return 1 if poly[0] > 0 else -1
    lead = poly[-1]
    sign = 1 if lead > 0 else -1
    if where == "neg_inf" and (len(poly) - 1) % 2:
        sign = -sign
    return sign


def variations(signs):
    return sum(signs[i] != signs[i + 1] for i in range(len(signs) - 1))


def check_iir(data, art):
    need(set(art) == {"stable", "jury_table", "schur_rows", "strict_margins", "bilinear_polynomial", "sturm_sequence", "sturm_variations", "route_agreement"}, "IIR top-level schema")
    original = [rat(v) for v in data["denominator_descending"]]
    need(len(original) == 19, "frozen IIR degree")
    rows = [original]
    margins = []
    jury = []
    while len(rows[-1]) > 1:
        row = rows[-1]
        margin = abs(row[0]) - abs(row[-1])
        need(margin > 0, "IIR strict Schur inequality")
        raw = [row[0] * row[i] - row[-1] * row[-1 - i] for i in range(len(row) - 1)]
        need(all(v.denominator == 1 for v in raw), "IIR normalization expects integer row")
        normalization_gcd = math.gcd(*[abs(v.numerator) for v in raw])
        need(normalization_gcd > 0, "IIR zero Schur row")
        nxt = [v / normalization_gcd for v in raw]
        margins.append(margin)
        jury.append({"forward": list(map(enc_fraction, row)), "reverse": list(map(enc_fraction, reversed(row))), "raw_normalization_gcd": normalization_gcd, "next": list(map(enc_fraction, nxt)), "endpoint_plus": enc_fraction(sum(row)), "endpoint_minus": enc_fraction(sum(((-1) ** (len(row) - 1 - i)) * row[i] for i in range(len(row)))), "strict_margin": enc_fraction(margin)})
        rows.append(nxt)
    need(art["stable"] is True, "IIR stable label")
    need(art["jury_table"] == jury, "IIR exact Jury table")
    need([[rat(v) for v in row] for row in art["schur_rows"]] == rows, "IIR Schur rows")
    need([rat(v) for v in art["strict_margins"]] == margins, "IIR strict witnesses")
    degree = len(original) - 1
    transformed_check = [Fraction() for _ in range(degree + 1)]
    for i, coefficient in enumerate(original):
        left = [Fraction(math.comb(degree - i, k)) for k in range(degree - i + 1)]
        right = [Fraction(math.comb(i, k) * ((-1) ** k)) for k in range(i + 1)]
        for a, x in enumerate(left):
            for b, y in enumerate(right):
                transformed_check[a + b] += coefficient * x * y
    transformed = [rat(v) for v in data["bilinear_polynomial_ascending"]]
    need(transformed == transformed_check, "IIR input bilinear polynomial does not match denominator")
    need([rat(v) for v in art["bilinear_polynomial"]] == transformed, "IIR pinned bilinear transform")
    sturm = sturm_sequence(transformed)
    need([[rat(v) for v in row] for row in art["sturm_sequence"]] == sturm, "IIR Sturm sequence")
    vneg = variations([sign_at(row, "neg_inf") for row in sturm])
    vzero = variations([sign_at(row, "zero") for row in sturm])
    vpos = variations([sign_at(row, "pos_inf") for row in sturm])
    counts = {"negative_infinite": vneg, "zero": vzero, "positive_infinite": vpos, "negative_roots": vneg - vzero, "positive_roots": vzero - vpos}
    need(art["sturm_variations"] == counts and counts["negative_roots"] == 18 and counts["positive_roots"] == 0, "IIR Sturm root counts")
    need(art["route_agreement"] == {"schur_stable": True, "bilinear_all_roots_negative": True}, "IIR dual-route agreement")


def enc_fraction(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


CHECKERS = {
    "P5ISO01": check_iso,
    "P5DMN02": check_dmn,
    "P5SYN03": check_syn,
    "P5VIT04": check_vit,
    "P5LIN10": check_lin,
    "P5KSX05": check_ksx,
    "P5MRK06": check_mrk,
    "P5NTT07": check_ntt,
    "P5LPC08": check_lpc,
    "P5IIR09": check_iir,
}


def main():
    if len(sys.argv) != 3:
        print(json.dumps({"accepted": False, "reason": "usage: judge TASK_DIR ARTIFACT"}))
        return 2
    task_dir, artifact_path = map(Path, sys.argv[1:])
    try:
        data = load(task_dir / "input.json")
        art = load(artifact_path)
        task_id = data.get("task_id")
        need(task_id in CHECKERS and task_dir.name == task_id, "task identity")
        CHECKERS[task_id](data, art)
    except (Reject, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"accepted": False, "reason": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps({"accepted": True, "task_id": task_id}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
