.PHONY: docs install lint test

all: install lint test

docs:
	sphinx-autobuild -z zxinglight/ docs/ docs/_build/html/

install:
	pip install -e .[test]

lint:
	flake8 zxinglight/ tests/ docs/ setup.py

test:
	nosetests tests/
