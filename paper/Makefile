PDF := mechanistic_localization_is_support_relative.pdf
BUILD := build
BIBTEX ?= $(shell command -v bibtex >/dev/null 2>&1 && echo bibtex || echo bibtex8)

.PHONY: all clean

all: $(PDF)

$(PDF): main.tex references.bib tmlr.sty tmlr.bst $(wildcard sections/*.tex)
	mkdir -p $(BUILD)
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	$(BIBTEX) $(BUILD)/main
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) main.tex
	cp $(BUILD)/main.pdf $(PDF)

clean:
	rm -rf $(BUILD) $(PDF)
