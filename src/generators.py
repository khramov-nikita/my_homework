from typing import Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator:
    """
    Функция возвращает итератор, где валюта соответствует заданной в параметре
    """
    if not transactions:
        raise TypeError("Пустой список транзакций")
    for dct in transactions:
        if dct["operationAmount"]["currency"]["code"] == currency_code:
            yield dct


def transaction_descriptions(transactions: list) -> Iterator:
    """
    Функция возвращает описание транзакций
    """
    for dct in transactions:
        if "description" in dct:
            yield dct["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Функция возвращает сгенерированный номер карты в формате **** **** **** ****
    в заданном числовом диапазоне
    """
    for x in range(start, stop + 1):
        card_number: str = f"{x:016}"
        formatted_number: str = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number
