install:
	pip install -e .
	pip install -r requirements-dev.txt

format:
	black .

lint:
	flake8 .

test:
	pytest -v

all: install format lint test