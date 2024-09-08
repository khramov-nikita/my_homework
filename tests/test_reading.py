import os
from typing import Any
from unittest.mock import patch

from pandas.core.frame import DataFrame

from src.reading import reading_csv, reading_excel

reading_path = os.path.abspath(__file__)
reading_csv_path = os.path.join(reading_path[:-22], "data", "test.csv")
reading_xlsx_path = os.path.join(reading_path[:-22], "data", "test.xlsx")


def test_read_csv(result_csv: list) -> None:
    assert reading_csv(reading_csv_path) == result_csv


def test_read_excel(result_excel: list) -> None:
    assert reading_excel(reading_xlsx_path) == result_excel


@patch("csv.DictReader")
def test_read_csv_mock(mock_csv: Any, result_csv: list) -> None:
    mock_csv.return_value = result_csv
    assert reading_csv(reading_csv_path) == result_csv
    mock_csv.assert_called_once()


@patch("pandas.read_excel")
def test_read_excel_mock(mock_excel: Any, result_excel_dataframe: DataFrame, result_excel: list) -> None:
    mock_excel.return_value = result_excel_dataframe
    assert reading_excel(reading_xlsx_path) == result_excel
    mock_excel.assert_called_once()
