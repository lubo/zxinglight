.PHONY: clean docs install lint test

all: install lint test

clean:
	rm -rf build dist docs/_build zxinglight/*.so

docs:
	sphinx-autobuild -z zxinglight/ docs/ docs/_build/html/

install:
	pip install -e .[test]

lint:
	flake8

test:
	nosetests tests/
