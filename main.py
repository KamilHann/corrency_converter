import requests
import json


def convert(from_cur: str, to_cur: str, amount: float = 1) -> float | None:
    rates = get_rates(from_cur)

    if type(rates) == dict:
        rate = rates[to_cur]

        return rate * amount


def get_rates(from_cur: str) -> dict | None:
    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"

    response = requests.get(url)

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        rates = json.loads(result)["rates"]

        return rates
