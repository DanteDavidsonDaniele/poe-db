# Python Project Template

Bare-bones, reusable scaffold: src layout, pyproject.toml, SQLite helper,
env-based config, pytest, ruff, Makefile.

## Structure

```
.
├── pyproject.toml      # deps, tooling config (one file for everything)
├── Makefile            # make setup / run / test / lint / fmt
├── .env.example        # copy to .env for local secrets/config
├── src/app/
│   ├── __init__.py
│   ├── config.py       # env-driven settings
│   ├── db.py           # SQLite connection helper + schema init
│   └── main.py         # entrypoint: python -m app.main
└── tests/
    └── test_smoke.py
```

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
