import requests
import json
import fastapi


def get_currencies():
    curs = []
    with open("currencies") as file:
        for line in file:
            cur = line.strip()
    return curs


def convert(from_cur: str, *to_cur: tuple[str]) -> float | None:
    rates = get_rates(from_cur)
    returning_rates = {}
    actual_curs = get_currencies()

    if type(rates) == dict:
        for cur in to_cur:
            if cur in actual_curs:
                returning_rates[cur] = rates[cur]

    return returning_rates


def get_rates(from_cur: str) -> dict | None:
    if from_cur not in get_currencies():
        return

    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"

    response = requests.get(url)

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        rates = json.loads(result)["rates"]

        return rates
