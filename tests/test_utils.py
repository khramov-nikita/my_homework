import os

from src.utils import convert_json

utils_path = os.path.abspath(__file__)
utils_test_empty_path = os.path.join(utils_path[:-20], "data", "test_empty.json")
utils_test_wrong_path = os.path.join(utils_path[:-20], "data", "test_wrong.json")
utils_not_path = os.path.join(utils_path[:-20], "data", "not_file.json")
utils_operations_path = os.path.join(utils_path[:-20], "data", "operations.json")


def test_convert_json_empty(error_state: list) -> None:
    assert convert_json(utils_test_empty_path) == error_state


def test_convert_json_wrong(error_state: list) -> None:
    assert convert_json(utils_test_wrong_path) == error_state


def test_convert_json_no_path(error_state: list) -> None:
    assert convert_json(utils_not_path) == error_state


def test_convert_json(correct_json: list) -> None:
    assert convert_json(utils_operations_path) == correct_json
