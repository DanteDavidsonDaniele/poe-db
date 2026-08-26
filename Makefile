.PHONY: setup run test lint fmt

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -e ".[dev]"
	cp -n .env.example .env || true

run:
	.venv/bin/python -m app.main

test:
	.venv/bin/pytest -v

lint:
	.venv/bin/ruff check .

fmt:
	.venv/bin/ruff format .
