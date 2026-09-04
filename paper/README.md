# Manuscript source

This directory contains the author-identified preprint source for *Mechanistic Localization Is Support-Relative*.

The scientific source was copied from the arXiv submission package used for the v1.0 public release, excluding macOS archive metadata. The anonymous TMLR review package is maintained separately.

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

The TMLR bibliography style is not vendored. The Makefile downloads `tmlr.bst` from the official `JmlrOrg/tmlr-style-file` repository at pinned commit `7bf90efe3a0debbba703c05c43f3ff7e4d4a2992` and verifies SHA-256 `694bb05ed86463c07ed93792fe2205d3e0f36eaac63e7d85a6ff85f3e85764aa`. That is the exact file present in the arXiv source package.

## Source organization

- `main.tex` — preprint wrapper, theorem environments, author metadata, abstract, section order
- `sections/` — scientific manuscript body
- `references.bib` — bibliography database
- `tmlr.sty` — TMLR style file from the preprint package
- `Makefile` — reproducible build with pinned, checksum-verified `tmlr.bst`

See the root [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) for style-file provenance and [`releases/v1.0/`](../releases/v1.0/) for source hashes.
