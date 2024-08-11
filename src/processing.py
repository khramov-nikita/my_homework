def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """
    Функция возвращает список словарей с соответствующим
    ключом 'state'
    """
    new_list: list = []
    for dct in dict_list:
        if "state" in dct:
            if dct["state"] == state:
                new_list.append(dct)
    return new_list


def sort_by_date(dct_list: list, state: bool = True) -> list:
    """
    Функция сортирует список словарей по ключу 'date'
    """
    for dct in dct_list:
        dct["date"] = dct["date"].replace("-", ".")
    new_list: list = sorted(dct_list, key=lambda dct: dct["date"], reverse=state)
    for dct in new_list:
        my_string = dct["date"]
        dct["date"] = f"{my_string[:4]}-{my_string[5:7]}-{my_string[8:]}"
    return new_list
