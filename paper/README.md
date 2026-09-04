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

## Source organization

- `main.tex` — preprint wrapper, theorem environments, author metadata, abstract, section order
- `sections/` — scientific manuscript body
- `references.bib` — bibliography database
- `tmlr.sty`, `tmlr.bst` — TMLR formatting files included in the preprint package

See the root [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) for style-file provenance and [`releases/v1.0/`](../releases/v1.0/) for source hashes.
