# v1.0 Public Release — September 2026

This directory records the provenance of the first public GitHub release of *Mechanistic Localization Is Support-Relative*.

## Public source

The author-identified wrapper, bibliography, scientific section files, and `tmlr.sty` are copied from the source package prepared for arXiv and supplied on September 4, 2026. macOS `__MACOSX` metadata from the ZIP archive was excluded. The nine scientific section files are Git-blob-identical to the validated TMLR manuscript body.

The `tmlr.bst` dependency from the preprint package is fetched at build time from the official `JmlrOrg/tmlr-style-file` repository at pinned commit `7bf90efe3a0debbba703c05c43f3ff7e4d4a2992`. Its Git blob SHA (`310ed3e74455269ad97d0b30639851af72cec965`) and SHA-256 (`694bb05ed86463c07ed93792fe2205d3e0f36eaac63e7d85a6ff85f3e85764aa`) match the file supplied in the preprint package.

## Review surface

The TMLR submission is maintained as an anonymous review package in a separate private research repository. That package, its generated submission ZIP, and review-administration metadata are not part of this public release.

## Hashes

[`SOURCE_SHA256SUMS.txt`](SOURCE_SHA256SUMS.txt) records SHA-256 hashes of the v1.0 preprint-package source files, including the original TMLR style files. The bibliography-style hash is also enforced by the public build even though that third-party file is fetched rather than vendored.

These hashes identify source files; a freshly compiled PDF need not be byte-identical across TeX installations because PDF metadata and toolchain behavior can vary.

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
