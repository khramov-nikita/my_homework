def get_mask_card_number(card_number: str) -> str:
    """Функция заменяет нужные числа на '*' и добавляет пробелы"""
    if len(card_number) == 16 and card_number.isdigit():
        mask_card_number: str = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return mask_card_number
    else:
        return "Неверные данные"


def get_mask_account(account: str) -> str:
    """Функция выводит последние 4 символа и добавляет '**' в начало"""
    if len(account) == 20 and account.isdigit():
        mask_account: str = f"**{account[-4:]}"
        return mask_account
    else:
        return "Неверные данные"
