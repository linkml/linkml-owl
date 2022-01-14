RUN = poetry run

all: EXAMPLES.md test

test:
	$(RUN) python -m unittest tests/test_*.py
#	$(RUN) pytest

tests/model/%.py: tests/model/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@

EXAMPLES.md: tests/output/owl_dumper_test.md
	cp $< $@
