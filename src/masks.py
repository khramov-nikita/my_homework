import logging

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename="../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция заменяет нужные числа на '*' и добавляет пробелы"""
    app_logger.info("Попытка форматирования номера карты")
    if len(card_number) == 16 and card_number.isdigit():
        app_logger.info("Успешное форматирование номера карты")
        mask_card_number: str = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return mask_card_number
    else:
        app_logger.error("Неверный номер карты")
        return "Неверные данные"


def get_mask_account(account: str) -> str:
    """Функция выводит последние 4 символа и добавляет '**' в начало"""
    app_logger.info("Попытка форматирования номера счёта")
    if len(account) == 20 and account.isdigit():
        app_logger.info("Успешное форматирование номера счёта")
        mask_account: str = f"**{account[-4:]}"
        return mask_account
    else:
        app_logger.error("Неверный номер счёта")
        return "Неверные данные"
