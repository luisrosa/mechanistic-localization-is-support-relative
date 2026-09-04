.PHONY: all check paper clean

all: check paper

check:
	python3 scripts/check_examples.py

paper:
	$(MAKE) -C paper

clean:
	$(MAKE) -C paper clean
