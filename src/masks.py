import logging
from typing import Optional

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Optional[str]) -> str:
    """Функция, скрывает символы номера карты и заменяет их на *"""
    if card_number is None:
        logger.error("Неправильно введён номер карты: значение None.")
        return "Неправильно введён номер карты!"

    card_number = card_number.replace(" ", "")

    if len(card_number) != 16 or not card_number.isdigit():
        logger.error(f"Неправильно введён номер карты: {card_number}.")
        return "Неправильно введён номер карты!"

    masked_number = list(card_number)  # Это список символов
    for pos in range(6, 12):
        masked_number[pos] = "*"

    masked_number_str = " ".join("".join(masked_number[i : i + 4]) for i in range(0, len(masked_number), 4))

    logger.info(f"Маскированный номер карты: {masked_number_str}.")
    return masked_number_str


# def get_mask_card_number(card_number: str) -> str:
#    """Функция, скрывает символы номера карты и заменяет их на *"""
#    if len(card_number) != 16 or not card_number.isdigit():
#        return 'Неправильно введён номер карты!'
#    else:
#        return card_number[0:6] + "*" * 6 + card_number[-4:]


def get_mask_account(cash_number: str | None) -> str:
    """Функция, принимает номер счета и создает маску из последних символов"""
    if cash_number is None:
        logger.error("Неправильно введён номер счета: значение None.")
        return "Неправильно введён номер счета!"

    if len(cash_number) <= 6 or not cash_number.isdigit():
        logger.error(f"Неправильно введён номер счета: {cash_number}.")
        return "Неправильно введён номер счета!"

    masked_account = "*" * 2 + cash_number[-4:]
    logger.info(f"Маскированный номер счета: {masked_account}.")
    return masked_account
