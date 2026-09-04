# Validation Record

## Public release

- Release: `v1.0`
- Date: September 2026
- Manuscript: *Mechanistic Localization Is Support-Relative*
- Author: Luis F. Rosario Freytes
- Public repository: `luisrosa/mechanistic-localization-is-support-relative`

## Source provenance

The author-identified wrapper, bibliography, scientific section files, and `tmlr.sty` under `paper/` were copied from the arXiv submission package supplied for this release, excluding macOS `__MACOSX` archive metadata. No scientific section was rewritten while constructing the public repository.

The arXiv package also bundled a `tmlr.bst` file; its package SHA-256 is retained in [`releases/v1.0/SOURCE_SHA256SUMS.txt`](releases/v1.0/SOURCE_SHA256SUMS.txt). The public repository does not vendor that third-party file. Instead, the build downloads the official TMLR bibliography style from `JmlrOrg/tmlr-style-file` at pinned commit `7bf90efe3a0debbba703c05c43f3ff7e4d4a2992`. The pinned dependency is therefore reproducible by Git revision without asserting byte identity with the copy bundled in the uploaded arXiv ZIP.

The anonymous TMLR review package is maintained separately in the private mechanistic-interpretability repository. Review-administration files and the anonymous submission ZIP are intentionally not duplicated here.

SHA-256 hashes for the v1.0 preprint package are recorded in [`releases/v1.0/SOURCE_SHA256SUMS.txt`](releases/v1.0/SOURCE_SHA256SUMS.txt).

## Executable finite checks

`scripts/check_examples.py` is the finite regression script used with the manuscript. It checks:

1. alternative minimal sufficient supports on a diagonal support;
2. disappearance of XOR dependence under support restriction;
3. the equivalence between direct one-coordinate operativity and membership in every minimal sufficient support across finite examples;
4. distributed XOR realization and strict decrease of localization order under restriction;
5. equivalence between receiver-family realization and the pair-cover formulation in the finite examples;
6. strict separation between source overlap and internal-state overlap;
7. a local-but-not-global realization example;
8. exhaustive verification of the cross-support union-compatibility criterion over all nonempty supports of a four-state binary ambient space for the implemented access/target family.

Run:

```bash
make check
```

Expected output:

```text
finite examples: PASS
```

## Build validation

The manuscript is compiled from `paper/main.tex` with the TMLR preprint style supplied in the arXiv package and the commit-pinned official TMLR bibliography style described above.

Run:

```bash
make paper
```

The target PDF is:

```text
paper/mechanistic_localization_is_support_relative.pdf
```

Before repository publication, the supplied preprint package was built locally. The finite regression suite returned `finite examples: PASS`; the identified manuscript compiled to 16 pages; and the final LaTeX log contained no unresolved references or citations.

GitHub Actions independently runs the finite checks and a clean LaTeX build using the repository's pinned external bibliography dependency. CI rejects compilation failures and unresolved references/citations detected in the final log. On `main`, a separate publishing workflow rebuilds the identified manuscript and commits the generated PDF when its bytes change.

## Release invariants

The v1.0 public release is intended to preserve the following invariants:

- the author-identified manuscript body remains the scientific source of record until an archival arXiv posting is available;
- private TMLR review administration is not published here;
- `CLAIMS.md` does not broaden the manuscript beyond exact interface realization;
- the finite regression script remains executable without external Python dependencies;
- the public PDF is generated from the repository manuscript source and commit-pinned official TMLR bibliography dependency;
- changes to theorem statements, examples, references, or scientific prose require a new provenance record rather than silent replacement.

## What validation does not establish

The regression suite is not a substitute for peer review or a proof assistant. It checks finite examples and executable equivalences used by the paper; the general theorems remain mathematical proofs in the manuscript.
