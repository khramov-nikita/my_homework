import pytest

from src.widget import get_date, mask_account_card


def test_mask_card(data_card: str, masked_card: str) -> None:
    assert mask_account_card(data_card) == masked_card
    return


def test_mask_account(data_account: str, masked_account: str) -> None:
    assert mask_account_card(data_account) == masked_account
    return


@pytest.mark.parametrize(
    "data, masked",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Maestro 159683786870519", "Неверные данные"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 68319824767376586", "Неверные данные"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 64686473678894779", "Неверные данные"),
        ("Счет", "Неверные данные"),
        ("64686473678894779589", "Неверные данные"),
        ("6473678894779589", "Неверные данные"),
        ("Счет 64686473678894779589262323452345", "Неверные данные"),
        ("64686473678894779589234523452", "Неверные данные"),
        ("aevaeroab oaavsodv oavosdv asdva", "Неверные данные"),
        ("1234 egra 1234 qwfr wrga", "Неверные данные"),
        (False, "Неверные данные"),
    ],
)
def test_mask_account_card(data: str, masked: str) -> None:
    assert mask_account_card(data) == masked
    return


@pytest.mark.parametrize(
    "date, masked_date",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2019.07.03", "03.07.2019"),
        ("qwsderfgfdsdf", "Неверные данные"),
        ("123.321.1.222", "Неверные данные"),
        ("npnarbnasvasvnnslnsbabssfbn", "Неверные данные"),
        ("2019 07 03", "03.07.2019"),
    ],
)
def test_get_date(date: str, masked_date: str) -> None:
    assert get_date(date) == masked_date
    return
