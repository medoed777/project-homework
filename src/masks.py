def get_mask_card_number(card_number: str) -> str:
    """Функция, скрывает символы номера карты и заменяет их на *"""
    if card_number is None:
        return "Неправильно введён номер карты!"

    card_number = card_number.replace(" ", "")

    if len(card_number) != 16 or not card_number.isdigit():
        return "Неправильно введён номер карты!"

    positions = [6, 7, 8, 9, 10, 11]
    list_number = list(card_number)

    for pos in positions:
        list_number[pos] = "*"

    masked_number = " ".join("".join(list_number[i : i + 4]) for i in range(0, len(list_number), 4))

    return masked_number


# def get_mask_card_number(card_number: str) -> str:
#    """Функция, скрывает символы номера карты и заменяет их на *"""
#    if len(card_number) != 16 or not card_number.isdigit():
#        return 'Неправильно введён номер карты!'
#    else:
#        return card_number[0:6] + "*" * 6 + card_number[-4:]


def get_mask_account(cash_number: str) -> str:
    """Функция, принимает номер счета и создает маску из последних символов"""
    if cash_number is None or len(cash_number) <= 6 or not cash_number.isdigit():
        return "Неправильно введён номер счета!"
    return "*" * 2 + cash_number[-4:]
