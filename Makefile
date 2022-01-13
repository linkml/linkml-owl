RUN = pipenv run

test:
	$(RUN) python -m unittest tests/test_*.py

tests/model/%.py: tests/model/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@
