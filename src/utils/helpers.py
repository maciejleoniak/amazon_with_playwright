# src/utils/helpers.py


def format_currency(value: str):
    return float(value.replace("$", "").replace(",", ""))
