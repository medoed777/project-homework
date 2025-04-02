from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(mask_card: str | None) -> str:
    """Функция обрабатывает информацию о картах и счетах."""
    if mask_card is None or mask_card.strip() == "":
        return ""

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


def get_date(iso_date: str | None) -> str:
    if iso_date is None or iso_date.strip() == "" or iso_date == int:
        raise ValueError("Неверный формат даты")

    try:
        date_obj = datetime.fromisoformat(iso_date.split("T")[0])
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")
