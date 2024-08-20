from src.utils import convert_json


def test_convert_json_empty(error_state) -> None:
    assert convert_json("../data/test_empty.json") == error_state


def test_convert_json_wrong(error_state) -> None:
    assert convert_json("../data/test_wrong.json") == error_state


def test_convert_json_no_path(error_state) -> None:
    assert convert_json("../data/not_file.json") == error_state


def test_convert_json(correct_json) -> None:
    assert convert_json("../data/operations.json") == correct_json
