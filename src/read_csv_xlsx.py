import pandas as pd


def read_csv_transactions(path_to_file_csv: str) -> list[dict]:
    """Функция считывает файл CSV и возвращает список транзакций в виде словаря"""
    try:
        data = pd.read_csv(path_to_file_csv)
        transactions = data.to_dict(orient='records')

        return transactions

    except FileNotFoundError:
        print(f"Файл не найден: {path_to_file_csv}")
        return []
    except pd.errors.EmptyDataError:
        print("Файл пуст.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


def read_xlsx_transactions(path_to_file_xlsx: str) -> list[dict]:
    """Считывает финансовые операции из файла Excel"""
    try:
        df = pd.read_excel(path_to_file_xlsx)

        transactions = df.to_dict(orient='records')

        return transactions

    except Exception as e:
        print(f"Ошибка при считывании файла: {e}")
        return []
