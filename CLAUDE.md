# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
make install   # pip install -e . && pip install -r requirements-dev.txt
```

## Common Commands

```bash
make format    # black .
make lint      # flake8 .
make test      # pytest -v
make all       # install + format + lint + test
```

Run a single test:
```bash
pytest tests/test_main.py::test_add -v
```

## Architecture

This is an early-stage MLOps demo project (end of chapter 1 of an MLOps book). The structure is minimal:

- `app/main.py` — application logic (currently a simple `add` function as a scaffold)
- `tests/test_main.py` — pytest tests importing from `app`
- Package is installed in editable mode via `setup.py` so `from app.main import ...` works in tests

## Code Style

- Line length: 88 (black/flake8 aligned)
- Formatting enforced by `black`; CI runs `flake8` and `pytest` on Python 3.9, 3.10, and 3.11
