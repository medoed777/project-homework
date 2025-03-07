from typing import List, Dict, Any, Iterator, Generator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Функция фильтрует транзакции по указанной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор для создания номеров банковских карт в заданном диапазоне."""
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
