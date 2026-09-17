# ls-safari

A Python testing safari — hunting down bugs and taming snakes with FastAPI, Pydantic, pytest, and uv.

## Before the session

```bash
git clone https://github.com/MattieBelt/ls-safari-workshop.git ls-safari
cd ls-safari
uv sync
```

That's it — you're ready.

## What you'll learn

- Why automated testing
- Unit testing
- Organizing & running multiple tests
- Test parametrization
- Fixtures
- Pydantic models and strict typing
- Unit testing a FastAPI dependency
- Mocking a dependency
- Testing routes with the FastAPI test client

## Structure

Each level in `levels/` is self-contained:

- `README.md` — goal, context, lesson, assignment
- starter code — small module (levels 1–4) or the shared example API (levels 5–8)
- assignment test file — TODOs to fill in

Work through levels in order. A level is done when its checklist passes.

## Example API

Levels 5–8 share one demo app in `app/` — CRUD, no auth:

- Two routers: `items`, `users` (`GET` list, `GET /{id}`, `POST`, `PUT /{id}`, `DELETE /{id}`)
- Simple dependency: `pagination_params` — pure function, no I/O
- Complex dependency: `get_db` — reads `app/data/db.json` (our "noSQL" store)
- Pydantic models: `Item`, `ItemCreate`, `User`, `UserCreate`

Simple vs. complex dependency is the split levels 6 and 7 are built around.

## Commands

```bash
uv run uvicorn app.main:app --reload         # run the example API (see /docs)
uv run pytest                                # run everything
uv run pytest levels/level_01_unit_testing   # run one level
```

## Levels

| Level | Goal | Time |
|---|---|---|
| [0 — Why testing?](levels/level_00_why_testing/README.md) | Motivation, no code | 10 min |
| [1 — Unit test](levels/level_01_unit_testing/README.md) | Your first pytest tests | 20 min |
| [2 — Run multiple tests](levels/level_02_multiple_tests/README.md) | Organizing & selecting tests | 20 min |
| [3 — Test parametrization](levels/level_03_parametrization/README.md) | `@pytest.mark.parametrize` | 15 min |
| [4 — Fixtures](levels/level_04_fixtures/README.md) | Extracting setup with `@pytest.fixture` | 15 min |
| [5 — Pydantic models and strict typing](levels/level_05_pydantic_models/README.md) | Testing validation rules you add | 25 min |
| [6 — Unit test a FastAPI dependency](levels/level_06_fastapi_dependency/README.md) | Testing a dependency directly | 15 min |
| [7 — Mock a sub dependency](levels/level_07_mocking/README.md) | Isolating tests from file I/O | 20 min |
| [8 — Test routes with the test client](levels/level_08_test_client/README.md) | End-to-end route testing | 25 min |

~2h45 of levels, solo work + a quick regroup each. Leaves room for an intro, breaks, and a
wrap-up in a half-day slot.
