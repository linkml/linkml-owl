DATA2OWL = poetry run python -m linkml_owl.owl_dumper

P01 = pizza01-toppings
P02 = pizza02-hasToppings
P03 = pizza03-countries
P04 = pizza04-refactored

pizza01.ofn: $(P01)-model.yaml $(P01)-data.yaml
	$(DATA2OWL) -s $^  -o $@
pizza02.ofn: $(P02)-model.yaml $(P02)-data.yaml
	$(DATA2OWL) -s $^  -o $@
pizza03.ofn: $(P03)-model.yaml $(P03)-data.yaml
	$(DATA2OWL) -s $^  -o $@
pizza04.ofn: $(P04)-model.yaml $(P04)-data.yaml
	$(DATA2OWL) -s $^  -o $@

%.owl: %.ofn
	robot convert -i $< -o $@
