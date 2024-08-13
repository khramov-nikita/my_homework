import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: str, masked_number: str) -> None:
    assert get_mask_card_number(card_number) == masked_number
    return


def test_get_mask_account(acc_number: str, masked_acc: str) -> None:
    assert get_mask_account(acc_number) == masked_acc
    return


@pytest.mark.parametrize(
    "number, result",
    [
        ("1234123412341234", "1234 12** **** 1234"),
        ("123123123331", "Неверные данные"),
        (" ", "Неверные данные"),
        ("abcdefg", "Неверные данные"),
        ("1234234234123412341234114321234123", "Неверные данные"),
    ],
)
def test_get_mask_card_number_2(number: str, result: str) -> None:
    assert get_mask_card_number(number) == result
    return


@pytest.mark.parametrize(
    "number, result",
    [
        ("73654108430135874305", "**4305"),
        ("12342134", "Неверные данные"),
        (" ", "Неверные данные"),
        ("abcdefg", "Неверные данные"),
        ("1234234234123412341234114321234123", "Неверные данные"),
    ],
)
def test_get_mask_account_number_2(number: str, result: str) -> None:
    assert get_mask_account(number) == result
    return
