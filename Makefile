RUN = poetry run

all: docs/examples.md test

test:
	$(RUN) pytest tests

tests/model/%.py: tests/model/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@


DOCTEST_DIR = linkml_owl
doctest:
	find $(DOCTEST_DIR) -type f \( -name "*.rst" -o -name "*.md" -o -name "*.py" \) -print0 | xargs -0 $(RUN) python -m doctest --option ELLIPSIS --option NORMALIZE_WHITESPACE

%-doctest: %
	$(RUN) python -m doctest --option ELLIPSIS --option NORMALIZE_WHITESPACE $<


# the examples.md file displayed on the site is generated
# from test_owl_dumper.py
docs/examples.md: tests/output/owl_dumper_test.md
	cp $< $@

example-docs docs/example-schema/index.md: tests/inputs/owl_dumper_test.yaml
	poetry run gen-doc --template-directory docgen-templates -d docs/example-schema $< 


serve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy


