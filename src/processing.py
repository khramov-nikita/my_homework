def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает список словарей с соответствующим
    ключом 'state'
    """
    new_list: list = []
    for dct in dict_list:
        if dct["state"] == state:
            new_list.append(dct)
    return new_list


def sort_by_date(dct_list: list, state: bool = True) -> list:
    """
    Функция сортирует список словарей по ключу 'date'
    """
    new_list: list = sorted(dct_list, key=lambda dct: dct["date"], reverse=state)
    return new_list
