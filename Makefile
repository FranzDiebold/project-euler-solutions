.PHONY: install
install:
	pip install -U pylint>=2.4.4

.PHONY: lint
lint:
	pylint --version
	pylint src/ --reports=yes
