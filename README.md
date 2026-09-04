# Mechanistic Localization Is Support-Relative

**Exact localization claims for supported neural processes**  
Luis F. Rosario Freytes, University of Michigan, Ann Arbor

**Current public release:** v1.0, September 2026.  
**Preprint:** arXiv posting pending; this repository is the current public manuscript source.  
**Submission status:** submitted to *Transactions on Machine Learning Research* (TMLR).  
**Peer-review status:** not yet peer reviewed.

## Read the paper

- [Current manuscript PDF](paper/mechanistic_localization_is_support_relative.pdf)
- [Current LaTeX source](paper/)
- [v1.0 provenance record](releases/v1.0/)
- [Claim ledger](CLAIMS.md)
- [Validation record](VALIDATION.md)

The `paper/` source is the author-identified preprint package prepared for arXiv, with macOS archive metadata removed. The anonymous TMLR review package and submission-administration materials are maintained separately and are not mirrored here.

## The problem: localization relative to what?

Mechanistic-interpretability studies routinely compare internal components across prompts, datasets, ablations, patches, and intervention protocols. Those comparisons implicitly choose a set of internal states on which the claimed mechanism must work.

The paper makes that state domain explicit.

A localization claim is not determined by network weights alone. At minimum it is typed by

```text
network parameters θ
+ represented cut q
+ analysis support S
+ phenomenon Φ
+ declared internal access L
--------------------------------
mechanistic-localization claim
```

For source-generated analyses, a prompt or input regime `C` induces the reachable support

$$
S_q^{\theta,C}=A_q^\theta(C),
$$

where $A_q^\theta$ is the prefix map to cut $q$. Interventions can instead specify an analysis support directly at an internal cut.

The central point is simple: **changing the supported state set can change the exact localization structure even when the network weights do not change.**

## The exact realization criterion

Fix an analysis support $S$, a phenomenon

$$
\Phi:S\to Y_\Phi,
$$

and a declared internal access

$$
L:S\twoheadrightarrow U.
$$

The access exactly realizes the phenomenon when there exists some $h$ with

$$
\Phi=hL.
$$

The paper proves the equivalent kernel criterion

$$
\boxed{\Phi=hL\quad\Longleftrightarrow\quad \ker L\subseteq\ker\Phi.}
$$

So exact localization is governed by which supported state pairs the access still identifies. If two supported states collide under $L$, they must also agree under the phenomenon.

This is an interface-sufficiency statement. It does not by itself assert causal necessity, a unique circuit, an algorithmic abstraction, or a human-interpretable explanation.

## A minimal example

Let

$$
x=(x_1,x_2)\in\mathbb R^2,
\qquad
\Phi(x)=x_1+x_2,
$$

with accesses $L_1(x)=x_1$ and $L_2(x)=x_2$.

- On all of $\mathbb R^2$, neither access alone determines $\Phi$; the joint access is required.
- On the diagonal $D=\{(t,t):t\in\mathbb R\}$, either coordinate alone determines $\Phi$ because $\Phi(t,t)=2t$.
- On the vertical support $V=\{(0,t):t\in\mathbb R\}$, the second coordinate alone suffices.

Nothing about the ambient formula or weights changed. The supported relations among internal states changed, and the localization changed with them.

## Declared receiver interfaces

At a network cut, the implementation supplies receiver maps

$$
X_q\xrightarrow{Q_{q,j}^\theta} Z_{q,j}
\xrightarrow{G_{q,j}^\theta}A_{q+1,j},
\qquad
F_{q,j}^\theta=G_{q,j}^\theta Q_{q,j}^\theta.
$$

The theory treats the $Q_{q,j}^\theta$ as declared boundary accesses: the actual interfaces through which downstream receivers obtain information. They are not arbitrary post-hoc factorizations chosen only to make a theorem go through.

Restricting a receiver to the support gives the receiver indistinguishability relation

$$
D_{q,j}^{\theta,C}
=
\ker\!\left(Q_{q,j}^\theta\big|_{S_q^{\theta,C}}\right).
$$

This makes support-relative receiver structure an explicit object of the analysis.

## Coordinate localization and supported operativity

For a coordinate subset $K$ at a cut, the paper defines $K$ to be sufficient for receiver $j$ when the supported receiver map factors through the coordinate projection $\pi_K$.

Equivalently,

$$
\ker(\pi_K|_S)\subseteq\ker(Q_j|_S).
$$

Inclusion-minimal sufficient coordinate sets form $\operatorname{MinSupp}$. A coordinate is directly operative exactly when it belongs to every minimal sufficient coordinate set. This separates three different notions that are easy to conflate:

- appearing in some minimal description,
- appearing in every minimal description,
- admitting a supported one-coordinate witness that changes the receiver while all other coordinates are fixed.

The last two coincide under the paper's finite-coordinate setup.

## Distributed realization and localization order

A phenomenon need not localize to one receiver. For a receiver family $K$, define the joint access by collecting the receiver outputs. Its kernel is

$$
\ker Q_{q,K}=\bigcap_{j\in K} D_{q,j}.
$$

The family realizes the phenomenon exactly when

$$
\bigcap_{j\in K}D_{q,j}\subseteq D_\Phi.
$$

The realizing-family set is upward closed, and the paper defines the exact localization order

$$
d_{\Phi,q}^{\theta,C}
=
\min\{|K|:K\text{ realizes }\Phi\},
$$

with the stated conventions for constant or unrealizable phenomena.

There is also a pair-cover form: each receiver separates some phenomenon-distinguished state pairs, and a receiver family realizes the phenomenon exactly when those separated-pair sets cover every pair that the phenomenon itself distinguishes.

## Support restriction changes feasible localization

For nested supports $C\subseteq C'$, every receiver family that realizes the phenomenon on the larger support also realizes it on the smaller support:

$$
\mathcal R_{\Phi,q}^{\theta,C'}
\subseteq
\mathcal R_{\Phi,q}^{\theta,C}.
$$

Therefore

$$
d_{\Phi,q}^{\theta,C}
\le
 d_{\Phi,q}^{\theta,C'}.
$$

A narrower support cannot increase the exact localization order. It can, however,

- decrease the required receiver count,
- create new minimal realizations,
- change which receiver family is minimal,
- make an apparently operative dependency disappear because the phenomenon becomes constant on the restricted support.

These changes require no weight update.

## Comparing different contexts

Nonnested supports require additional care.

### Source overlap can understate internal-state overlap

For source regimes $C$ and $D$,

$$
S_q^{\theta,C\cap D}
\subseteq
S_q^{\theta,C}\cap S_q^{\theta,D}.
$$

The inclusion can be strict when the prefix map is noninjective. Two disjoint source classes can therefore reach the same represented internal state.

### Local realization need not extend to the union

Suppose the same access $L$ realizes the same phenomenon $\Phi$ separately on supports $S_1$ and $S_2$. That does not guarantee realization on $S_1\cup S_2$.

The local realizations extend to the union exactly when every cross-support collision is phenomenon-consistent:

$$
x\in S_1,\ y\in S_2,\ L(x)=L(y)
\quad\Longrightarrow\quad
\Phi(x)=\Phi(y).
$$

The obstruction is not failure on either context individually. It is a new collision created only when the contexts are compared together.

## What the paper establishes

The manuscript develops the following exact results in the stated deterministic, set-theoretic regime:

1. Source regimes generate reachable supports, while interventions may define cut-local analysis supports directly.
2. Exact phenomenon realization through a declared access is equivalent to kernel inclusion.
3. The same criterion extends to distributed receiver families through intersections of receiver kernels.
4. Coordinate sufficiency has an exact kernel criterion, and direct supported operativity is characterized by membership in every minimal sufficient support.
5. Realizing receiver families are upward closed and admit a pair-cover characterization.
6. Restricting support can only enlarge the feasible realization family, so exact localization order cannot increase under restriction.
7. Minimal realization identity can change without changing either network weights or localization order.
8. Input/source overlap and represented-state overlap need not coincide.
9. Separate local realizations extend to a union exactly when cross-support access collisions are phenomenon-consistent.

## Scope

The paper is intentionally exact and set-theoretic. It does not assume linearity, differentiability, a finite activation alphabet, or a probability distribution over the support.

It also does not identify exact interface realization with:

- causal necessity,
- intervention control,
- a unique mechanistic circuit,
- algorithmic abstraction,
- equivalence between competing presentation languages,
- human interpretability.

Those require additional structure. Approximate and probabilistic versions of the support-relative theory are left open.

## Validation

The repository includes executable finite regression checks for the paper's finite examples and equivalences:

```bash
make check
```

The checks cover alternative/minimal supports, disappearing dependencies, direct operativity, distributed XOR localization, pair-cover equivalence, source/internal overlap, local-but-not-global realization, and exhaustive verification of the cross-support compatibility criterion on a finite ambient state space.

To compile the manuscript locally:

```bash
make paper
```

See [VALIDATION.md](VALIDATION.md) for the release invariants and [releases/v1.0/](releases/v1.0/) for source hashes.

## Repository organization

- `paper/` — author-identified preprint source and compiled manuscript
- `scripts/check_examples.py` — finite exhaustive/regression checks used during manuscript validation
- `releases/v1.0/` — source provenance and SHA-256 hashes
- `CLAIMS.md` — semantic claim ledger and explicit nonclaims
- `VALIDATION.md` — release and validation record
- `.github/workflows/validate.yml` — CI for checks and LaTeX compilation

The broader mechanistic-interpretability research program from which this paper emerged is deliberately not duplicated here. This repository is the focused public release for *Mechanistic Localization Is Support-Relative*.

## Citation

Until an archival preprint identifier is assigned, cite the manuscript as:

```bibtex
@article{rosariofreytes2026mechanistic,
  title  = {Mechanistic Localization Is Support-Relative},
  author = {Rosario Freytes, Luis F.},
  year   = {2026},
  note   = {Preprint; submitted to Transactions on Machine Learning Research}
}
```

Machine-readable citation metadata are provided in [CITATION.cff](CITATION.cff). The arXiv identifier will be added when the pending posting becomes public.

## License

The author's manuscript source, validation code, and repository documentation are released under the [Creative Commons Attribution 4.0 International License](LICENSE). Third-party TMLR style files retain their upstream terms; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
