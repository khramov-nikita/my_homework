import os
from functools import wraps
from typing import Any, Callable, Optional

decor_path = os.path.abspath(__file__)


def log(filename: Optional[str] = None) -> Callable:
    """
    Записывает вызов функции и ее результат в файл или в консоль
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                raise e
            else:
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
                return result
            finally:
                if filename:
                    with open(os.path.join(decor_path[:-18], "data", f"{filename}"), "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return wrapper

    return decorator
