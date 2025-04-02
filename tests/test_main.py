from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx import read_csv_transactions, read_xlsx_transactions
from src.utils import load_transactions


def test_filter_by_state() -> None:
    transactions = [
        {
            "date": "2023-01-01",
            "description": "Транзакция 1",
            "operationAmount": {"amount": 100, "currency": {"name": "RUB"}},
            "state": "EXECUTED",
            "from": "Счет 1234",
            "to": "Счет 5678",
        },
        {
            "date": "2023-01-02",
            "description": "Транзакция 2",
            "operationAmount": {"amount": 200, "currency": {"name": "RUB"}},
            "state": "CANCELED",
            "from": "Счет 2345",
            "to": "Счет 6789",
        },
        {
            "date": "2023-01-03",
            "description": "Транзакция 3",
            "operationAmount": {"amount": 300, "currency": {"name": "USD"}},
            "state": "EXECUTED",
            "from": "",
            "to": "Счет 7890",
        },
    ]

    executed_transactions = filter_by_state(transactions, state="EXECUTED")
    assert len(executed_transactions) == 2


def test_sort_by_date() -> None:
    transactions = [
        {
            "date": "2023-01-01",
            "description": "Транзакция 1",
            "operationAmount": {"amount": 100, "currency": {"name": "RUB"}},
            "state": "EXECUTED",
            "from": "Счет 1234",
            "to": "Счет 5678",
        },
        {
            "date": "2023-01-02",
            "description": "Транзакция 2",
            "operationAmount": {"amount": 200, "currency": {"name": "RUB"}},
            "state": "CANCELED",
            "from": "Счет 2345",
            "to": "Счет 6789",
        },
        {
            "date": "2023-01-03",
            "description": "Транзакция 3",
            "operationAmount": {"amount": 300, "currency": {"name": "USD"}},
            "state": "EXECUTED",
            "from": "",
            "to": "Счет 7890",
        },
    ]

    sorted_transactions = sort_by_date(transactions, reverse=False)
    assert sorted_transactions[0]["date"] == "2023-01-01"


def test_load_transactions() -> None:
    transactions = load_transactions("path/to/test_transactions.json")
    assert isinstance(transactions, list)


def test_read_csv_transactions() -> None:
    transactions = read_csv_transactions("path/to/test_transactions.csv")
    assert isinstance(transactions, list)


def test_read_xlsx_transactions() -> None:
    transactions = read_xlsx_transactions("path/to/test_transactions_excel.xlsx")
    assert isinstance(transactions, list)
