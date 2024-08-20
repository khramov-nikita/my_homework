from unittest.mock import patch
from src.external_api import transaction_sum
from typing import Any


@patch("requests.get")
def test_transaction_sum(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "RUB", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1724197444, "rate": 1},
        "date": "2024-08-20",
        "result": 31957.58,
    }
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
