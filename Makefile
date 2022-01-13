RUN = pipenv run

all: EXAMPLES.md test

test:
	$(RUN) python -m unittest tests/test_*.py

tests/model/%.py: tests/model/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@

EXAMPLES.md: tests/output/owl_dumper_test.md
	cp $< $@
