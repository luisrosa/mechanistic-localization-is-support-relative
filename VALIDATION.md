# Validation Record

## Public release

- Release: `v1.0`
- Date: September 2026
- Manuscript: *Mechanistic Localization Is Support-Relative*
- Author: Luis F. Rosario Freytes
- Public repository: `luisrosa/mechanistic-localization-is-support-relative`

## Source provenance

The files under `paper/` were copied from the author-identified arXiv submission package supplied for this release, excluding macOS `__MACOSX` archive metadata. No scientific section was rewritten while constructing the public repository.

The anonymous TMLR review package is maintained separately in the private mechanistic-interpretability repository. Review-administration files and the anonymous submission ZIP are intentionally not duplicated here.

SHA-256 hashes for the v1.0 paper source are recorded in [`releases/v1.0/SOURCE_SHA256SUMS.txt`](releases/v1.0/SOURCE_SHA256SUMS.txt).

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

The manuscript is compiled from `paper/main.tex` with the TMLR preprint style distributed in the arXiv source package.

Run:

```bash
make paper
```

The target PDF is:

```text
paper/mechanistic_localization_is_support_relative.pdf
```

GitHub Actions runs both the finite checks and a clean LaTeX build. CI rejects compilation failures and unresolved references/citations detected in the final log.

## Release invariants

The v1.0 public release is intended to preserve the following invariants:

- author-identified preprint source remains the scientific source of record until an archival arXiv posting is available;
- private TMLR review administration is not published here;
- `CLAIMS.md` does not broaden the manuscript beyond exact interface realization;
- the finite regression script remains executable without external Python dependencies;
- the compiled public PDF is produced from the checked-in source;
- changes to theorem statements, examples, references, or scientific prose require a new provenance record rather than silent replacement.

## What validation does not establish

The regression suite is not a substitute for peer review or a proof assistant. It checks finite examples and executable equivalences used by the paper; the general theorems remain mathematical proofs in the manuscript.
