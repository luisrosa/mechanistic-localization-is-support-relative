# Third-Party Notices

The manuscript uses TMLR formatting files needed to reproduce the preprint build.

## `paper/tmlr.sty`

TMLR LaTeX style file distributed by *Transactions on Machine Learning Research*. The file identifies itself as adapted by Hugo Larochelle and Fabian Pedregosa from ICLR style macros with material from JMLR macros. The copy checked into this repository is the file supplied in the manuscript's TMLR/arXiv source package. It is not relicensed by the author under the repository's CC BY 4.0 license.

## `tmlr.bst`

The TMLR bibliography style is derived from the `plainnat`/ICML style lineage. Its header states that it may be redistributed and/or modified under the LaTeX Project Public License, version 1 or any later version.

Rather than vendor the file, `paper/Makefile` downloads it from the official `JmlrOrg/tmlr-style-file` repository at commit `7bf90efe3a0debbba703c05c43f3ff7e4d4a2992`. The uploaded arXiv source package bundled a separate copy of `tmlr.bst`; that package copy is recorded in the v1.0 source hashes, while the public repository build uses the commit-pinned official dependency.

## Python and LaTeX dependencies

Python standard-library modules and the LaTeX packages loaded by `paper/main.tex` are external dependencies and are not distributed as original work of this repository.

The repository-level CC BY 4.0 license applies to the author's manuscript source, original validation code, and repository documentation, excluding third-party materials that carry their own terms.
