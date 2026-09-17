def apply_discount(total: float, percent: float) -> float:
    """Apply a percentage discount to a total.

    Raises ValueError if percent is not between 0 and 100 (inclusive).
    """
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return total - (total * percent / 100)
