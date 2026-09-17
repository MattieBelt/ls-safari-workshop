def calculate_total(prices: list[float]) -> float:
    """Sum a list of prices. An empty list totals 0."""
    return sum(prices)


def add_item(prices: list[float], price: float) -> list[float]:
    """Return a new price list with `price` appended.

    Raises ValueError if price is negative.
    """
    if price < 0:
        raise ValueError("price must not be negative")
    return [*prices, price]
