.PHONY: docs install lint test

all: install lint test

docs:
	sphinx-autobuild -z zxinglight/ docs/ docs/_build/html/

install:
	pip install -e .[test]

lint:
	flake8

test:
	nosetests tests/
