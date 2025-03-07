import pytest

from src.generators import filter_by_currency

@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00.000000",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Тестовая транзакция",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321"
        }
    ]

def test_filter_by_currency_usd(transactions):
    result = list(filter_by_currency(transactions, 'USD'))
    assert len(result) == 2
    assert result[0]['id'] == 1
    assert result[1]['id'] == 3

def test_filter_by_currency_eur(transactions):
    result = list(filter_by_currency(transactions, 'EUR'))
    assert len(result) == 1
    assert result[0]['id'] == 2

def test_filter_by_currency_non_existent(transactions):
    result = list(filter_by_currency(transactions, 'GBP'))
    assert len(result) == 0