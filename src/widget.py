from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскирует номер счета или карты в зависимости от ввода"""
    if not account_card:
        return "Неверные данные"
    split_data: list = str(account_card).split()
    if split_data[0].isalpha() and split_data[-1].isdigit():
        if account_card[0:4] == "Счет" and len(account_card[5:]) == 20:
            split_acc = split_data
            split_acc[-1] = get_mask_account(split_acc[-1])
            if split_acc[-1][0] == "*":
                mask_acc: str = " ".join(split_acc)
                return mask_acc
            else:
                acc_number: str = split_acc[-1]
                return acc_number
        else:
            split_card = split_data
            split_card[-1] = get_mask_card_number(split_card[-1])
            if split_card[-1][-5] == " ":
                mask_card: str = " ".join(split_card)
                return mask_card
            else:
                card_number: str = split_card[-1]
                return card_number
    else:
        return "Неверные данные"


def get_date(date: str) -> str:
    """Функция форматирует дату в виде ДД.ММ.ГГГГ"""
    if not date:
        return "Неверные данные"
    if len(date) >= 10 and not f"{date[8:10]}{date[5:7]}{date[:4]}".isdigit():
        return "Неверные данные"
    result: str = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return result
