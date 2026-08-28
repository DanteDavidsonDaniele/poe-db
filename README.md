# Python Project Template

Bare-bones, reusable scaffold: src layout, pyproject.toml, SQLite helper,
env-based config, pytest, ruff, Makefile.

## Structure

model - defines database schema
repository - defines methods relating to database interactions
router - defines API endpoints
service - defines methods relating to business logic
util - defines unviversal helper methods 




## Quick start

```bash
make setup    # venv + install deps (editable) + create .env
make run      # runs src/app/main.py
make test     # pytest
make lint     # ruff check
make fmt      # ruff format
```

Without make: `python3 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"`.

## Reusing this template

1. Copy the folder, rename `src/app` to your package name
2. Find/replace `app` in pyproject.toml, Makefile, and imports
3. Add real dependencies to `[project] dependencies` in pyproject.toml
4. Extend `init_db()` in db.py with your actual schema
