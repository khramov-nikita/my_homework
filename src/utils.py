import csv
import json
import logging
import os

import pandas as pd
from pandas.core.frame import DataFrame

utils_path = os.path.abspath(__file__)
utils_log_path = os.path.join(utils_path[:-13], "logs", "utils.log")

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=utils_log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def reading_json(path: str) -> list:
    """
    Функция принимает путь к json файлу и конвертирует указанный файл в python объект
    """

    try:
        app_logger.info("Попытка загрузки json фала")
        with open(path, encoding="utf-8") as f:
            result: list = json.load(f)
    except Exception as e:
        app_logger.error(f"Неудачная попытка загрузки json файла: {e}")
        return []
    else:
        app_logger.info("Успешная загрузка json файла")
        return result


def reading_csv(path: str) -> list:
    """
    Функция считывает CSV файл и возвращает список словарей.
    """
    result = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            result.append(row)
        return result


def reading_excel(path: str) -> list:
    """
    Функция считывает XLSX файл и возвращает список словарей.
    """
    excel_data: DataFrame = pd.read_excel(path)
    result: list = excel_data.to_dict(orient="records")
    return result
