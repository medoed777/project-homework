import pytest

from src.decorators import log


@log(filename="test_mylog.txt")
def add(x: int, y: int) -> int:
    return x + y


@log(filename="test_mylog.txt")
def divide(x: int, y: int) -> float:
    return x / y


def test_add() -> None:
    result = add(1, 2)
    assert result == 3

    with open("test_mylog.txt") as f:
        log_content = f.read()
    assert "add ok" in log_content


def test_divide() -> None:
    result = divide(4, 2)
    assert result == 2

    with open("test_mylog.txt") as f:
        log_content = f.read()
    assert "divide ok" in log_content


def test_divide_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    with open("test_mylog.txt") as f:
        log_content = f.read()
    assert "divide error: ZeroDivisionError" in log_content
