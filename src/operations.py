import re
from collections import Counter
from typing import Dict, List


def filtered_operations(operations: list[dict], search_string: str) -> list[dict]:
    """Ищет транзакции по описанию, используя регулярные выражения."""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [operation for operation in operations if pattern.search(operation.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict], categories: Dict[str, List[str]]) -> Dict[str, int]:
    """Подсчитывает количество транзакций по категориям."""
    counter: Dict[str, int] = Counter()

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category, keywords in categories.items():
            if any(keyword.lower() in description for keyword in keywords):
                counter[category] += 1

    return dict(counter)
