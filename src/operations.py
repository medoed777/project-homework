import re
from collections import Counter


def filtered_operations(transactions: list[dict], search_string: str) -> list[dict]:
    """Ищет транзакции по описанию, используя регулярные выражения."""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]
