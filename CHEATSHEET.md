# Cheatsheet

Handy commands for guiding/running the session.

## Introduction

Before diving in:

- Welcome + quick check: did everyone's `git clone` + `uv sync` go through cleanly?
- Show the finished app running (`uv run uvicorn app.main:app --reload`, hit `/docs`): a
  sneak peek of what they'll be testing by the end
- Walk through the README together: What you'll learn, Structure, the Levels table (goal +
  time per level)
- Give everyone a couple of minutes to skim their own copy and get their editor/terminal ready
- Kick off Level 0: Why testing?

## Running tests

```bash
# whole suite, all levels
uv run pytest

# one level
uv run pytest levels/level_0X_...

# per-test pass/fail listing, nicer to screen-share than dots
uv run pytest levels/level_0X_... -v

# name match (level 2's lesson)
uv run pytest -k <name>

# exact node id (level 2's lesson)
uv run pytest <path>::<Class>::<test>

# list discovered tests without running
uv run pytest --collect-only -q

# stop at the first failure, good for pausing on one live
uv run pytest -x
```

## Facilitator only

```bash
# level 0's live bug demo, prints -5.0
uv run python levels/level_00_why_testing/demo.py

# boot the API, then hit /docs for live requests
uv run uvicorn app.main:app --reload

# reveal a fully green run, then back to starter
git checkout solutions && uv run pytest && git checkout main

# peek at one solved file without switching branches
git show solutions:levels/level_0X_.../test_foo.py

# reset seed data after a live demo mutates it
git checkout -- app/data/db.json
```
