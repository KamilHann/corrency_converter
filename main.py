import requests


def get_api_key() -> str:
    with open("apikey") as file:
        key = file.read()

    if key:
        return key


def get_rate(from_cur: str, to_cur: str, amount: float = 1) -> float | None:
    url = url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_cur}&from={from_cur}&amount={amount}"

    payload = {}
    headers = {
        "apikey": get_api_key()
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    if status_code == 200:
        return result
