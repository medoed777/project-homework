from src.generators import filter_by_currency
from src.operations import filtered_operations
from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx import read_csv_transactions, read_xlsx_transactions
from src.utils import load_transactions
from src.widget import get_date, mask_account_card


def main() -> None:
    """Функция для запуска приложения в пользовательском интерфейсе"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    transactions = []

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Пользователь: ")

        if choice in ["1", "2", "3"]:
            file_path = input("Введите путь к файлу: ")
            try:
                if choice == "1":
                    transactions = load_transactions(file_path)
                elif choice == "2":
                    transactions = read_csv_transactions(file_path)
                elif choice == "3":
                    transactions = read_xlsx_transactions(file_path)

                if not transactions:
                    print("Файл не содержит транзакций.")
                    continue

                break
            except Exception as e:
                print(f"Ошибка при загрузке транзакций: {e}")
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_input = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ")
        status = status_input.upper()

        if status in valid_states:
            filtered_transactions = filter_by_state(transactions, state=status)
            break
        else:
            print(f"Статус операции {status_input} недоступен.")

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order_choice = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        reverse = order_choice in ["убыванию", "по убыванию"]
        filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse)

    currency_filter_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if currency_filter_choice == "да":
        filtered_transactions = filter_by_currency(filtered_transactions, "RUB")

    search_choice = input("Хотите выполнить поиск по описанию транзакций? Да/Нет\nПользователь: ").strip().lower()
    if search_choice == "да":
        search_string = input("Введите строку для поиска:\nПользователь: ")
        filtered_transactions = filtered_operations(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            date = get_date(transaction["date"])
            description = transaction.get("description", "Без описания")
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
            if "from" in transaction:
                account_from = mask_account_card(transaction["from"])
            else:
                account_from = ""
            account_to = mask_account_card(transaction.get("to", "Счет **0000"))

            if account_from:
                output_line = f"{date} {description}\n{account_from} -> {account_to}"
            else:
                output_line = f"{date} {description}\n{account_to}"

            print(f"{output_line}\nСумма: {amount} {currency}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
