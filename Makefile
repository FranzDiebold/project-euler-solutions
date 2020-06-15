.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: lint
lint:
	pylint --version
	pylint src/ --reports=yes

.PHONY: test
test:
	pytest test/
