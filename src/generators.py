from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict[str, str]], currency: str) -> Iterator[Dict[str, str]]:
    """Функция фильтрует транзакции по указанной валюте."""
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction