# Level 0: Why testing?

**Goal:** understand why we write automated tests, before writing any.

## Try it yourself

```bash
uv run python levels/level_00_why_testing/demo.py
```

`demo.py`:

```python
def apply_discount(total: float, percent: float) -> float:
    return total - (total * percent / 100)
```

Output: `-5.0`. A customer gets *paid* €5 to buy a €10 item. Looked fine, "worked when I
tried it", shipped. Nobody notices for a sprint.

Manual testing only catches what you're looking for, on the day you look. It misses:

- the same bug coming back after a "harmless" refactor
- edge cases nobody thought to click through (0%, 100%, negative input)
- regressions in unrelated code that shares a function

## Lesson

Why testing matters, day to day:

- **A safety net**: refactor with confidence, know instantly if something broke
- **Executable documentation**: a test shows what a function is supposed to do
- **Fast feedback**: seconds, not minutes of manual clicking
- **Confidence to ship**: "tests pass" beats "seemed fine"

Why it's standard industry practice, not optional polish:

- **Cost of bugs grows over time**: a bug caught while coding costs minutes; the same bug
  caught in production costs an incident, a hotfix, and support tickets ("shift-left" testing)
- **Enables CI/CD**: pipelines gate deploys on tests, so no tests means no safe automation
- **Team scale**: many people can touch the same codebase without breaking each other silently
- **Compliance**: regulated industries (finance, healthcare, aviation) often require test
  evidence as audit trails
- **Better design**: testable code tends to be more modular and decoupled (the core argument
  behind TDD)

## Assignment

None, discussion only. What's a bug you shipped that a test would've caught?

Next: [Level 1: Unit test](../level_01_unit_testing/README.md)
