# Level 2 — Run multiple tests

**Goal:** organize a growing test suite two ways — separate files, and classes — and run a
subset of it.

## Context

`pricing_suite/` is a small package: `basket.py` (`calculate_total`, `add_item`) and
`discounts.py` (`apply_discount`, from level 1).

Real apps don't keep every test in one file. Imagine adding 3 small util functions to a
FastAPI app that already has 400 tests — you don't bolt them onto one giant file, you add a
`test_utils.py` next to the module they test.

## Lesson

**Method 1 — separate files**, one per source module. The default: mirror your source layout,
one test file per module. `test_discounts.py` tests `pricing_suite/discounts.py` and lives
apart from `test_basket.py`. No wiring needed — pytest just collects every `test_*.py` it
finds.

**Method 2 — classes**, for grouping closely related tests inside one of those files, once it's
carrying more than one function worth separating (see `test_basket.py`):

```python
class TestCalculateTotal:
    def test_sums_prices(self):
        assert calculate_total([1.0, 2.0]) == 3.0
```

Reach for separate files first; add classes inside a file once it needs that extra structure.

Ways to run a subset:

- By file: `uv run pytest levels/level_02_multiple_tests/test_basket.py`
- By name match: `uv run pytest -k calculate_total`
- By node id: `uv run pytest levels/level_02_multiple_tests/test_basket.py::TestAddItem::test_add_item_appends_price`

Add `-v` for a per-test pass/fail listing.

## Assignment

Complete the TODOs in both `test_basket.py` and `test_discounts.py`:

- [ ] `calculate_total` — sums a non-empty list
- [ ] `calculate_total` — empty list totals to 0
- [ ] `add_item` — appends a price
- [ ] `add_item` — rejects a negative price with `ValueError`
- [ ] `apply_discount` — happy path
- [ ] `apply_discount` — rejects an out-of-range percent

**Bonus — VS Code Test Explorer:** run/debug the same tests from the sidebar instead of the
terminal. `.vscode/settings.json` (already in the repo) enables it:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": []
}
```

The interpreter path is the part that usually trips people up: without it, VS Code runs tests
with your system Python, which doesn't have pytest installed (only `.venv`, from `uv sync`,
does). Open the **Testing** sidebar (flask icon) — tests should appear automatically.

Next: [Level 3 — Test parametrization](../level_03_parametrization/README.md)
