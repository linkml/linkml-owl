# Note: this Makefile is aimed primarily at developers of linkml-owl
RUN = poetry run

all: doc/examples.md test

test:
	$(RUN) python -m unittest tests/test_*.py
#	$(RUN) pytest

tests/model/%.py: tests/model/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@

doc/examples.md: tests/output/owl_dumper_test.md
	cp $< $@

serve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy
