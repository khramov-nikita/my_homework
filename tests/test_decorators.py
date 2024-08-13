from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> None:
    @log(filename="test_log.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out

    try:
        my_function(1, "t")
    except TypeError:
        captured = capsys.readouterr()
        assert (
            "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs:(1, 't'), {}\n"
            in captured.out
        )
