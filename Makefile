venv ?= .venv

.DEFAULT_GOAL := all

config:
	@rm -rf $(venv) && python -m venv $(venv)
	@$(venv)/bin/pip install -r requirements.txt
	@$(venv)/bin/pip install -r requirements-dev.txt

run:
	@$(venv)/bin/python -m webapp.app

test:
	@$(venv)/bin/python -m pytest -v -s

lint:
	@$(venv)/bin/python -m flake8 webapp
	@$(venv)/bin/python -m mypy webapp

all: lint test
