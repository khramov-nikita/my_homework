import csv

import pandas as pd
from pandas.core.frame import DataFrame


def reading_csv(path: str) -> list:
    result = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            result.append(row)
        return result


def reading_excel(path: str) -> list:
    excel_data: DataFrame = pd.read_excel(path)
    result: list = excel_data.to_dict(orient="records")
    return result
