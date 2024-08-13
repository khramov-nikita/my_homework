import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_dict: list, filtered_executed: list, filtered_canceled: list) -> None:
    assert filter_by_state(list_of_dict, state="EXECUTED") == filtered_executed
    assert filter_by_state(list_of_dict, state="CANCELED") == filtered_canceled
    return


def test_filter_by_state_no_state(list_of_dict_no_state: list, error_state: list) -> None:
    assert filter_by_state(list_of_dict_no_state, state="EXECUTED") == error_state
    assert filter_by_state(list_of_dict_no_state, state="CANCELED") == error_state
    return


@pytest.mark.parametrize(
    "dct, new_state, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
        ),
        (
            [
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
    ],
)
def test_filter_by_state_parametrize(dct: list, new_state: str, result: list) -> None:
    assert filter_by_state(dct, state=new_state) == result
    return


def test_sort_by_date(list_of_dict: list, sorted_by_date: list) -> None:
    assert sort_by_date(list_of_dict) == sorted_by_date
    return


def test_sort_by_date_direction(list_of_dict: list, sorted_by_date_reverse: list) -> None:
    assert sort_by_date(list_of_dict, state=False) == sorted_by_date_reverse
    return


def test_sort_by_date_same_date(list_of_dict_same_date: list, list_of_dict_same_date_result: list) -> None:
    assert sort_by_date(list_of_dict_same_date) == list_of_dict_same_date_result
    return


@pytest.mark.parametrize(
    "dct, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018.06.30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018.10.14"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date_parameterise(dct: list, result: list) -> None:
    assert sort_by_date(dct) == result
    return
