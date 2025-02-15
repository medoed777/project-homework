from datetime import datetime
from src.masks import *


def mask_account_card(mask_card: str) -> str:
    """Функция, обрабатывает информацию о картах и счетах"""
    card = mask_card.split()
    card_type = " ".join(card[:-1])
    number = card[-1]

    if "Счет" in mask_card:
        return f"{card_type} {get_mask_account(number)}"

    else:
        return f"{card_type} {get_mask_card_number(number)}"



def get_date(iso_date: str) -> str:
    """Функция, обрабатывают дату ISO формата"""
    date = datetime.fromisoformat(iso_date)
    formated_date = date.strftime("%d.%m.%y")
    return formated_date
