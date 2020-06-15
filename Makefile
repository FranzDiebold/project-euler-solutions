.PHONY: install
install:
	pip install -U pylint>=2.5.3

.PHONY: lint
lint:
	pylint --version
	pylint src/ --reports=yes
