# Claim Ledger

This file records the semantic commitments of *Mechanistic Localization Is Support-Relative*. It is meant to keep the public repository aligned with the manuscript's actual theorem regime.

## Core objects

1. **Support is an explicit argument of a localization claim.** A source regime `C` induces a reachable support at a represented cut; an intervention may instead provide an analysis support directly at that cut.
2. **Phenomenon and access are separate declarations.** A phenomenon `Φ:S→Y_Φ` specifies what must be preserved; an access `L:S→U` specifies what internal information is allowed to realize it.
3. **Receiver interfaces are declared by the network decomposition under study.** The framework does not allow arbitrary post-hoc access maps to stand in for architectural receivers without saying so.

## Exact realization

4. **Exact interface realization means factorization.** `L` realizes `Φ` on `S` exactly when `Φ=h∘L` for some `h`.
5. **Kernel inclusion is necessary and sufficient.** Exact realization holds iff `Ker L ⊆ Ker Φ`.
6. **Exact realization is support-relative.** The criterion is evaluated only on supported state pairs.

## Coordinate and receiver localization

7. **Coordinate sufficiency is a factorization statement.** A coordinate set `K` is sufficient for a receiver exactly when the supported receiver map factors through the projection to `K`.
8. **Minimal sufficient coordinate sets are inclusion-minimal, not merely minimum-cardinality sets.**
9. **Direct supported operativity is characterized by every-minimal-support membership.** In the manuscript's finite-coordinate setup, coordinate `i` has a one-coordinate supported witness for a receiver exactly when `i` belongs to every minimal sufficient coordinate set.
10. **Distributed realization is allowed.** A receiver family realizes a phenomenon when the intersection of its receiver indistinguishability relations refines the phenomenon relation.
11. **Localization order is only a receiver-count statistic relative to a declared decomposition.** It is not a coordinate-free measure of mechanism complexity.
12. **Realizing receiver families are upward closed.** Adding receivers cannot destroy exact realization.
13. **The pair-cover formulation is equivalent to kernel inclusion.** A family realizes the phenomenon exactly when its receivers collectively separate every supported state pair distinguished by the phenomenon.

## Support restriction

14. **Restriction enlarges the feasible realization family.** If `C⊆C'`, every realization valid on `C'` remains valid on `C`.
15. **Exact localization order cannot increase under support restriction.** `d(C)≤d(C')` for nested supports in the paper's setup.
16. **Minimal realization identity can change while the weights stay fixed.** Restriction may create alternative minimal realizations even when localization order does not change.
17. **A dependency can disappear under restriction.** If the supported phenomenon becomes constant, the empty access can suffice.

## Cross-context comparison

18. **Source overlap need not equal internal-state overlap.** `S(C∩D)⊆S(C)∩S(D)`, with strict inclusion possible under a noninjective prefix.
19. **Disjoint source classes may share represented internal states.** This follows from noninjective source-to-cut maps.
20. **Local realization on two supports does not imply realization on their union.**
21. **Union extension is controlled exactly by cross-support collisions.** Given separate local realizations through the same access, realization extends to the union iff equal access values across the two supports imply equal phenomenon values.

## Explicit nonclaims

The paper does **not** claim that exact interface realization is equivalent to any of the following:

- causal necessity;
- causal sufficiency under arbitrary interventions;
- a unique circuit or unique mechanistic decomposition;
- algorithmic abstraction;
- feature identity across representation changes;
- equivalence between competing interpretability vocabularies;
- human-readable explanation;
- approximate or probabilistic faithfulness.

The paper also does not claim that every useful mechanistic-interpretability method must be formulated with kernels. Kernel language is the exact set-theoretic representation used for the stated factorization questions.

## Regime

The main results are exact and deterministic. Supports may contain arbitrary coordinate values, including real-valued activations. The results do not require linearity, differentiability, a finite activation alphabet, or a probability distribution. Recurrent, stochastic, tool-using, and training-time processes require an expanded process model beyond the finite feed-forward setup developed here.
