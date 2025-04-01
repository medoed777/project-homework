from typing import Any, Dict, List

import pytest

from src.operations import count_transactions_by_category, filtered_operations


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


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "description": "Перевод на счет", "amount": 100},
        {"id": 2, "description": "Оплата коммунальных услуг", "amount": 50},
        {"id": 3, "description": "Перевод на счет", "amount": 200},
        {"id": 4, "description": "Купон на скидку", "amount": 10},
        {"id": 5, "description": "Оплата газа", "amount": 30},
    ]


@pytest.fixture
def categories() -> Dict[str, List[str]]:
    return {
        "Переводы": ["перевод"],
        "Коммунальные услуги": ["коммунальных", "газа"],
        "Скидки": ["скидка"],
    }


@pytest.mark.parametrize(
    "transactions, expected_result",
    [
        (
            [
                {"id": 1, "description": "Перевод на счет", "amount": 100},
                {"id": 2, "description": "Оплата коммунальных услуг", "amount": 50},
                {"id": 3, "description": "Перевод на счет", "amount": 200},
                {"id": 4, "description": "Купон на скидку", "amount": 10},
                {"id": 5, "description": "Оплата газа", "amount": 30},
            ],
            {"Переводы": 2, "Коммунальные услуги": 2},
        ),
        ([], {}),
    ],
)
def test_count_transactions(
    transactions: List[Dict[str, Any]], expected_result: Dict[str, int], categories: Dict[str, List[str]]
) -> None:
    result = count_transactions_by_category(transactions, categories)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_no_matching_categories(sample_transactions: List[Dict[str, Any]], categories: Dict[str, List[str]]) -> None:
    transactions_no_match = [
        {"id": 1, "description": "Неизвестная операция", "amount": 100},
    ]

    result = count_transactions_by_category(transactions_no_match, categories)
    assert result == {}, f"Expected an empty dict, but got {result}"
