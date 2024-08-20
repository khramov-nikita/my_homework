import os

import requests
from dotenv import load_dotenv


def transaction_sum(transaction: dict) -> float:
    """
    Функция возвращает сумму трансакции, если трансакция совершена не в рублях,
    то конвертирует её в рубли
    """

    load_dotenv()
    payload = {
        "amount": transaction["operationAmount"]["amount"],
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB",
    }
    headers = {"apikey": os.getenv("API_KEY")}
    http = "https://api.apilayer.com/exchangerates_data/convert"
    response = requests.get(http, headers=headers, params=payload)
    dict_response = response.json()
    result: float = dict_response["result"]
    return result
