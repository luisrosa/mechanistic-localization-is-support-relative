# v1.0 Public Release — September 2026

This directory records the provenance of the first public GitHub release of *Mechanistic Localization Is Support-Relative*.

## Public source

The author-identified wrapper, bibliography, scientific section files, and `tmlr.sty` are copied from the source package prepared for arXiv and supplied on September 4, 2026. macOS `__MACOSX` metadata from the ZIP archive was excluded. The nine scientific section files are Git-blob-identical to the validated TMLR manuscript body.

The uploaded preprint package also contained a `tmlr.bst` file, whose SHA-256 is retained in [`SOURCE_SHA256SUMS.txt`](SOURCE_SHA256SUMS.txt). The public repository does not vendor that third-party file. Its build instead fetches the official TMLR bibliography style from `JmlrOrg/tmlr-style-file` at pinned commit `7bf90efe3a0debbba703c05c43f3ff7e4d4a2992`.

## Review surface

The TMLR submission is maintained as an anonymous review package in a separate private research repository. That package, its generated submission ZIP, and review-administration metadata are not part of this public release.

## Hashes

[`SOURCE_SHA256SUMS.txt`](SOURCE_SHA256SUMS.txt) records SHA-256 hashes of the v1.0 uploaded preprint-package source files, including the template files that were present in that archive. These hashes are a provenance record for the supplied package; they should not be read as hashes of every external dependency downloaded by the public build.

A freshly compiled PDF also need not be byte-identical across TeX installations because PDF metadata and toolchain behavior can vary.

## Scientific scope

The release corresponds to the manuscript whose main exact claims are:

- support is an explicit argument of mechanistic-localization claims;
- exact realization through an access is equivalent to kernel inclusion;
- distributed realization is characterized by intersections of receiver kernels;
- exact localization order cannot increase under support restriction;
- minimal realization identity may change without a weight change;
- source overlap can understate represented-state overlap;
- separate local realizations extend to a union exactly when cross-support access collisions are phenomenon-consistent.

For the full semantic ledger and nonclaims, see [`CLAIMS.md`](../../CLAIMS.md).
