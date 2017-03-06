.PHONY: install lint test

all: install lint test

install:
	pip install -e .[test]

lint:
	flake8 zxinglight/ tests/ setup.py

test:
	nosetests tests/
