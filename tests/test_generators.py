from typing import Any, Dict, List, Tuple

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00.000000",
            "operationAmount": {"amount": "1000.00", "currency": {"name": "USD", "code": "USD"}},
            "description": "Тестовая транзакция",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321",
        },
    ]


def test_filter_by_currency_usd(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_eur(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "EUR"))
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_currency_non_existent(transactions: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, "GBP"))
    assert len(result) == 0


def test_empty_transaction_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


@pytest.fixture
def expected_outputs() -> Dict[Tuple[int, int], List[str]]:
    return {
        (1, 5): [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ],
        (10000, 10001): ["0000 0000 0001 0000", "0000 0000 0001 0001"],
        (5, 1): [],
        (1, 1): ["0000 0000 0000 0001"],
    }


@pytest.mark.parametrize("start, end", [(1, 5), (10000, 10001), (5, 1), (1, 1)])
def test_card_number_generator(expected_outputs: Dict[Tuple[int, int], List[str]], start: int, end: int) -> None:
    result = list(card_number_generator(start, end))
    assert result == expected_outputs[(start, end)]


@pytest.mark.parametrize("number", [0, 9999999999999999])
def test_formatting(number: int) -> None:
    formatted_number = (
        f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:]
    )
    assert len(formatted_number.replace(" ", "")) == 16


@pytest.fixture
def transaction_data() -> Any:
    return {
        "with_descriptions": [
            {"amount": 100, "date": "2023-01-01", "description": "Оплата за услуги"},
            {"amount": 200, "date": "2023-01-02", "description": "Перевод"},
        ],
        "without_descriptions": [
            {"amount": 100, "date": "2023-01-01"},
            {"amount": 200, "date": "2023-01-02"},
        ],
        "mixed": [
            {"amount": 100, "date": "2023-01-01", "description": "Оплата за услуги"},
            {"amount": 200, "date": "2023-01-02"},
            {"amount": 300, "date": "2023-01-03", "description": "Перевод"},
        ],
        "empty": [],
    }


@pytest.mark.parametrize(
    "data_key, expected",
    [
        ("with_descriptions", ["Оплата за услуги", "Перевод"]),
        ("without_descriptions", ["Нет описания", "Нет описания"]),
        ("mixed", ["Оплата за услуги", "Нет описания", "Перевод"]),
        ("empty", []),
    ],
)
def test_transaction_descriptions(transaction_data: Dict[str, List[Any]], data_key: str, expected: Any) -> None:
    transactions = transaction_data[data_key]
    result = list(transaction_descriptions(transactions))
    assert result == expected
