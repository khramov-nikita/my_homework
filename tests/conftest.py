import pytest


@pytest.fixture
def card_number() -> str:
    return "1234123412341234"


@pytest.fixture
def masked_number() -> str:
    return "1234 12** **** 1234"


@pytest.fixture
def acc_number() -> str:
    return "12341234123412341234"


@pytest.fixture
def masked_acc() -> str:
    return "**1234"
