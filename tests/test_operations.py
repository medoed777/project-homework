import pytest

from src.operations import filtered_operations


def test_filter_operations() -> None:
    operations = [
        {"id": 1, "description": "Перевод на счет", "amount": 100},
        {"id": 2, "description": "Оплата коммунальных услуг", "amount": 50},
        {"id": 3, "description": "Перевод между счетами", "amount": 200},
        {"id": 4, "description": "Купон на скидку", "amount": 10},
    ]

    result = filtered_operations(operations, "Перевод на счет")
    assert len(result) == 1
    assert result[0]["id"] == 1

    result = filtered_operations(operations, "Перевод")
    assert len(result) == 2
    assert {op["id"] for op in result} == {1, 3}

    result = filtered_operations(operations, "оплата")
    assert len(result) == 1
    assert result[0]["id"] == 2

    result = filtered_operations(operations, "не существует")
    assert len(result) == 0

    result = filtered_operations(operations, "")
    assert len(result) == len(operations)

    result = filtered_operations(operations, r"счет")
    assert len(result) == 2
    assert {op["id"] for op in result} == {1, 3}
