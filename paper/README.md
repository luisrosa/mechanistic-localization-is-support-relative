# Manuscript source

This directory contains the author-identified preprint source for *Mechanistic Localization Is Support-Relative*.

The author wrapper, bibliography, scientific section files, and `tmlr.sty` were copied from the arXiv submission package used for the v1.0 public release, excluding macOS archive metadata. The anonymous TMLR review package is maintained separately.

## Build

From the repository root:

```bash
make paper
```

or from this directory:

```bash
make
```

The result is `mechanistic_localization_is_support_relative.pdf`.

The TMLR bibliography style is treated as an external build dependency rather than vendored. The Makefile downloads `tmlr.bst` from the official `JmlrOrg/tmlr-style-file` repository at pinned commit `7bf90efe3a0debbba703c05c43f3ff7e4d4a2992`. The arXiv ZIP bundled its own `tmlr.bst`; its SHA-256 remains recorded in the v1.0 source-package provenance, but the public repository build intentionally uses the pinned official dependency.

## Source organization

- `main.tex` — preprint wrapper, theorem environments, author metadata, abstract, section order
- `sections/` — scientific manuscript body
- `references.bib` — bibliography database
- `tmlr.sty` — TMLR style file from the preprint package
- `Makefile` — reproducible build with a commit-pinned official `tmlr.bst`

See the root [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) for style-file provenance and [`releases/v1.0/`](../releases/v1.0/) for source hashes.
