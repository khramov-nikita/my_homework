import json


def convert_json(json_data: str) -> list:
    """
    Функция принимает путь к json файлу и конвертирует указанный файл в python объект
    """

    try:
        with open(json_data, encoding="utf-8") as f:
            result: list = json.load(f)
    except Exception:
        return []
    else:
        return result
