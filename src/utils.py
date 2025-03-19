import json
import requests
import os


def load_transactions(file_path: str | None) -> list[dict] | None:
    if not os.path.isfile(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []



