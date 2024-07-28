from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    if account_card[0:4] == 'Счет':
        return f'Счет {get_mask_account(account_card)}'
    else:
        split_card: list = account_card.split()
        split_card[-1]: str = get_mask_card_number(split_card[-1])
        mask_card: str = ' '.join(split_card)
        return mask_card


def get_date(date: str) -> str:
    result: str = f'{date[8:10]}.{date[5:7]}.{date[:4]}'
    return result
