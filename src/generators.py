from typing import Any, Dict, Generator, Iterator, List, Union


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Any:
    """Функция фильтрует транзакции по указанной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор для создания номеров банковских карт в заданном диапазоне."""
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"


def transaction_descriptions(
    transactions: list[dict[str, int | float | str]],
) -> Generator[Union[int, float, str], None, None]:
    """Генератор, возвращает описание операций"""
    for transaction in transactions:
        description = transaction.get("description")
        if description is None:
            description = "Нет описания"
        yield description
