PDF := mechanistic_localization_is_support_relative.pdf
BUILD := build
BIBTEX ?= $(shell command -v bibtex >/dev/null 2>&1 && echo bibtex || echo bibtex8)
TMLR_STYLE_COMMIT := 7bf90efe3a0debbba703c05c43f3ff7e4d4a2992
TMLR_BST_URL := https://raw.githubusercontent.com/JmlrOrg/tmlr-style-file/$(TMLR_STYLE_COMMIT)/tmlr.bst

.PHONY: all clean

all: $(PDF)

tmlr.bst:
	curl -fsSL $(TMLR_BST_URL) -o $@

$(PDF): main.tex references.bib tmlr.sty tmlr.bst $(wildcard sections/*.tex)
	mkdir -p $(BUILD)
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	$(BIBTEX) $(BUILD)/main
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	cp $(BUILD)/main.pdf $(PDF)

clean:
	rm -rf $(BUILD) $(PDF) tmlr.bst
