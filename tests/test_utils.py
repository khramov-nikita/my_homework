import os
from typing import Any
from unittest.mock import patch

from pandas.core.frame import DataFrame

from src.utils import reading_csv, reading_excel, reading_json

utils_path = os.path.abspath(__file__)
reading_csv_path = os.path.join(utils_path[:-20], "data", "test.csv")
reading_xlsx_path = os.path.join(utils_path[:-20], "data", "test.xlsx")
utils_test_empty_path = os.path.join(utils_path[:-20], "data", "test_empty.json")
utils_test_wrong_path = os.path.join(utils_path[:-20], "data", "test_wrong.json")
utils_not_path = os.path.join(utils_path[:-20], "data", "not_file.json")
utils_operations_path = os.path.join(utils_path[:-20], "data", "operations.json")


def test_reading_json_empty(error_state: list) -> None:
    assert reading_json(utils_test_empty_path) == error_state


def test_reading_json_wrong(error_state: list) -> None:
    assert reading_json(utils_test_wrong_path) == error_state


def test_reading_json_no_path(error_state: list) -> None:
    assert reading_json(utils_not_path) == error_state


def test_reading_json(correct_json: list) -> None:
    assert reading_json(utils_operations_path) == correct_json


def test_reading_csv(result_csv: list) -> None:
    assert reading_csv(reading_csv_path) == result_csv


def test_reading_excel(result_excel: list) -> None:
    assert reading_excel(reading_xlsx_path) == result_excel


@patch("csv.DictReader")
def test_reading_csv_mock(mock_csv: Any, result_csv: list) -> None:
    mock_csv.return_value = result_csv
    assert reading_csv(reading_csv_path) == result_csv
    mock_csv.assert_called_once()


@patch("pandas.read_excel")
def test_reading_excel_mock(mock_excel: Any, result_excel_dataframe: DataFrame, result_excel: list) -> None:
    mock_excel.return_value = result_excel_dataframe
    assert reading_excel(reading_xlsx_path) == result_excel
    mock_excel.assert_called_once()
