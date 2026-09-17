def apply_discount(total: float, percent: float) -> float:
    return total - (total * percent / 100)


if __name__ == "__main__":
    print(apply_discount(10, 150))
