from typing import Any
from unittest.mock import patch

from src.external_api import transaction_sum


@patch("requests.get")
def test_transaction_sum(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1724249237, "rate": 91.350022},
        "date": "2024-08-21",
        "result": 751022.33037,
    }
    assert (
        transaction_sum(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 751022.33037
    )


@patch("requests.get")
def test_transactions_sum_rub(mock_get: Any) -> None:
    assert (
        transaction_sum(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )
    mock_get.assert_not_called()
