def get_mask_card_number(card_number: str) -> str:
    """Функция заменяет нужные числа на '*' и добавляет пробелы"""
    symbols: list[str] = []
    for symbol in card_number:
        symbols += symbol
    count: int = 0
    for number in range(len(symbols)):
        if 6 <= count <= 11:
            symbols[number] = "*"
        count += 1
    for index in range(3):
        symbols.insert((-4) * (index + 1) - index, " ")
    mask_card_number: str = "".join(symbols)
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция выводит последние 4 символа и добавляет '**' в начало"""
    end_part: str = account[-4:]
    result: str = "**" + end_part
    return result
