def get_mask_card_number(card_number: str) -> str:
    """Функция заменяет нужные числа на '*' и добавляет пробелы"""
    mask_card_number: str = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция выводит последние 4 символа и добавляет '**' в начало"""
    mask_account: str = f"**{account[-4:]}"
    return mask_account
