TAX_RATES = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4,
}


def calculate_tax(amount: float, province: str, hour: int) -> float:
    taxes = amount * (TAX_RATES.get(province, 0) * (hour / 24.0))
    return round(amount + taxes, 2)
