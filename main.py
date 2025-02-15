from src.widget import get_mask_account, get_mask_card_number, mask_account_card, get_date

if __name__ == "__main__":
    card_nums = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 715830073472346758",
        "Счет 3538303347444789556068768",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 7365"
    ]

    for card in card_nums:
        print(mask_account_card(card))
