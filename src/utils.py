import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.isfile(file_path):
        logger.warning(f"Файл не найден: {file_path}. Возвращается пустой список.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружены данные из файла: {file_path}.")
                return data
            else:
                logger.error(f"Данные в файле {file_path} не являются списком. Возвращается пустой список.")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}.")
        return []
    except IOError as e:
        logger.error(f"Ошибка ввода-вывода при чтении файла {file_path}: {e}.")
        return []
