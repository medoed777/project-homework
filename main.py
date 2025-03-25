from src.external_api import conversion_currency
from src.decorators import log
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, card_number_generator, transaction_descriptions

if __name__ == "__main__":
    card_nums = [
        "Maestro 1596837868705199",
        "Счет 9589",
        "MasterCard 715830073472346758",
        "Счет 3538303347444789556068768",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 1234123412347365",
        "Счёт 1234",
        "Счёт 1234123412347362626335",
        "",
        "Карта",
        "Карта ",
        "Счёт",
        "Счет ",
    ]

    for card in card_nums:
        print(mask_account_card(card))

print(get_date("2025-06-03T02:26:18.671407"))



dict_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(dict_list, state="EXECUTED"))
print(sort_by_date(dict_list, False))

transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

for card_number in card_number_generator(1, 5):
    print(card_number)

descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)


@log(filename="mylog.txt")
def my_function_with(x: int, y: int) -> float:
    return x / y


# my_function_with(1, 0)



transactions = load_transactions("data/operations.json")
print(transactions)


transaction_example = {"amount": 1000000000.0, "currency": "USD"}

result = conversion_currency(transaction_example)
if result is not None:
    print(f"Сумма транзакции в рублях: {result:.2f} RUB")