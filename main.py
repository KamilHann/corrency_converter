import requests
import json
import fastapi


def convert(from_cur: str, *to_cur: tuple[str]) -> float | None:
    rates = get_rates(from_cur)
    returning_rates = {}

    if type(rates) == dict:
        for cur in to_cur:
            rate = rates[cur]

            returning_rates[cur] = rate

    return returning_rates


def get_rates(from_cur: str) -> dict | None:
    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"

    response = requests.get(url)

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        rates = json.loads(result)["rates"]

        return rates
