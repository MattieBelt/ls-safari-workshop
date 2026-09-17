class Cart:
    def __init__(self):
        self.items: list[float] = []

    def add(self, price: float) -> None:
        self.items.append(price)

    def total(self) -> float:
        return sum(self.items)
