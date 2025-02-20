from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

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

print(get_date("2025-06-03T02:26:18.671407"))

dict_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(dict_list, state='EXECUTED'))
print(sort_by_date(dict_list, False))