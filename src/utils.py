import json
import logging

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename="../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def convert_json(json_data: str) -> list:
    """
    Функция принимает путь к json файлу и конвертирует указанный файл в python объект
    """

    try:
        app_logger.info("Попытка загрузки json фала")
        with open(json_data, encoding="utf-8") as f:
            result: list = json.load(f)
    except Exception:
        app_logger.error("Неудачная попытка json файла")
        return []
    else:
        app_logger.info("Успешная загрузка json файла")
        return result
