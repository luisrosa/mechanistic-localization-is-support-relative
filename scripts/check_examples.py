#!/usr/bin/env python3
"""Exhaustive checks for finite examples in the TMLR theory draft."""

from itertools import combinations, product


def kernel(domain, fn):
    return {(x, y) for x in domain for y in domain if fn(x) == fn(y)}


def factors_through(domain, access, target):
    return kernel(domain, access) <= kernel(domain, target)


def projection(indices):
    return lambda x: tuple(x[i] for i in indices)


def minimal_sufficient_supports(domain, fn, ncoords):
    sufficient = []
    for r in range(ncoords + 1):
        for coords in combinations(range(ncoords), r):
            if factors_through(domain, projection(coords), fn):
                sufficient.append(frozenset(coords))
    return {k for k in sufficient if not any(j < k for j in sufficient)}


def direct_witness(domain, fn, i):
    return any(
        all(x[k] == y[k] for k in range(len(x)) if k != i)
        and fn(x) != fn(y)
        for x in domain
        for y in domain
    )


def realizing_families(domain, receivers, target):
    out = set()
    for r in range(len(receivers) + 1):
        for idxs in combinations(range(len(receivers)), r):
            access = lambda x, idxs=idxs: tuple(receivers[i](x) for i in idxs)
            if factors_through(domain, access, target):
                out.add(frozenset(idxs))
    return out


def realization_order(domain, receivers, target):
    fam = realizing_families(domain, receivers, target)
    return min(map(len, fam)) if fam else float("inf")


def pair_cover_realizes(domain, receivers, target, idxs):
    distinguished = {
        (x, y) for x in domain for y in domain if target(x) != target(y)
    }
    separated = set()
    for i in idxs:
        separated |= {
            (x, y)
            for x, y in distinguished
            if receivers[i](x) != receivers[i](y)
        }
    return distinguished <= separated


def cross_support_compatible(s1, s2, access, target):
    return all(
        access(x) != access(y) or target(x) == target(y)
        for x in s1
        for y in s2
    )


def test_alternative_and_disappearing_supports():
    square = list(product([0, 1], repeat=2))
    diagonal = [(0, 0), (1, 1)]

    q_first = lambda x: x[0]
    assert minimal_sufficient_supports(square, q_first, 2) == {frozenset({0})}
    assert minimal_sufficient_supports(diagonal, q_first, 2) == {
        frozenset({0}),
        frozenset({1}),
    }

    parity = lambda x: x[0] ^ x[1]
    assert minimal_sufficient_supports(square, parity, 2) == {frozenset({0, 1})}
    assert minimal_sufficient_supports(diagonal, parity, 2) == {frozenset()}


def test_direct_operativity_equals_every_minimal_support():
    domains = [
        list(product([0, 1], repeat=2)),
        [(0, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 1)],
    ]
    functions = [
        lambda x: x[0],
        lambda x: x[0] ^ x[1],
        lambda x: x[0] & x[1],
    ]
    for domain in domains:
        for fn in functions:
            mins = minimal_sufficient_supports(domain, fn, 2)
            for i in range(2):
                assert direct_witness(domain, fn, i) == all(i in k for k in mins)


def test_distributed_xor_and_strict_order():
    square = list(product([0, 1], repeat=2))
    row = [(0, 0), (0, 1)]
    parity = lambda x: x[0] ^ x[1]
    receivers = [lambda x: x[0], lambda x: x[1]]

    assert realization_order(square, receivers, parity) == 2
    assert realization_order(row, receivers, parity) == 1
    assert realizing_families(square, receivers, parity) <= realizing_families(
        row, receivers, parity
    )

    for domain in (square, row):
        realized = realizing_families(domain, receivers, parity)
        for r in range(len(receivers) + 1):
            for idxs in combinations(range(len(receivers)), r):
                assert (frozenset(idxs) in realized) == pair_cover_realizes(
                    domain, receivers, parity, idxs
                )


def test_source_overlap():
    c1, c2 = {"a"}, {"b"}
    prefix = lambda _x: "z"
    image = lambda c: {prefix(x) for x in c}
    assert c1 & c2 == set()
    assert image(c1 & c2) == set()
    assert image(c1) & image(c2) == {"z"}


def test_local_not_global():
    u1 = [(0, 0), (1, 1)]
    u2 = [(0, 0), (2, 1)]
    overlap = sorted(set(u1) & set(u2))
    union = sorted(set(u1) | set(u2))
    q = lambda x: x[0]
    second = lambda x: x[1]

    assert factors_through(u1, second, q)
    assert factors_through(u2, second, q)
    assert factors_through(overlap, second, q)
    assert not cross_support_compatible(u1, u2, second, q)
    assert not factors_through(union, second, q)


def test_cross_support_criterion_exhaustively():
    ambient = list(product([0, 1], repeat=2))
    supports = [
        [x for x, keep in zip(ambient, mask) if keep]
        for mask in product([False, True], repeat=len(ambient))
        if any(mask)
    ]
    accesses = [
        lambda x: x[0],
        lambda x: x[1],
        lambda x: x[0] ^ x[1],
    ]
    targets = [
        lambda x: x[0],
        lambda x: x[1],
        lambda x: x[0] ^ x[1],
        lambda x: x[0] & x[1],
    ]

    for s1 in supports:
        for s2 in supports:
            union = sorted(set(s1) | set(s2))
            for access in accesses:
                for target in targets:
                    if factors_through(s1, access, target) and factors_through(
                        s2, access, target
                    ):
                        assert factors_through(
                            union, access, target
                        ) == cross_support_compatible(s1, s2, access, target)


def main():
    test_alternative_and_disappearing_supports()
    test_direct_operativity_equals_every_minimal_support()
    test_distributed_xor_and_strict_order()
    test_source_overlap()
    test_local_not_global()
    test_cross_support_criterion_exhaustively()
    print("finite examples: PASS")


if __name__ == "__main__":
    main()
