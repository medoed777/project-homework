from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_card: str) -> str:
    """Функция обрабатывает информацию о картах и счетах."""
    account_keywords = ["Счет", "Счёт"]
    card = mask_card.split()
    card_type = " ".join(card[:-1])
    number = card[-1]

    is_account = any(account in mask_card for account in account_keywords)

    if is_account:
        if "Неправильно введён номер счета!" in get_mask_account(number):
            return "Неправильно введён номер счета!"
        return f"{card_type} {get_mask_account(number)}"
    else:
        if "Неправильно введён номер карты!" in get_mask_card_number(number):
            return "Неправильно введён номер карты!"
        return f"{card_type} {get_mask_card_number(number)}"


def get_date(iso_date: str) -> str:
    """Функция, обрабатывают дату ISO формата"""
    date = datetime.fromisoformat(iso_date)
    formated_date = date.strftime("%d.%m.%Y")
    return formated_date
