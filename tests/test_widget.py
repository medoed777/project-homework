import pytest
from src.widget import mask_account_card, get_date


card_nums = [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 9589", "Неправильно введён номер счета!"),
    ("MasterCard 715830073472346758", "Неправильно введён номер карты!"),
    ("Счет 3538303347444789556068768", "Счет **8768"),
    ("Счёт 1234", "Неправильно введён номер счета!"),
    ("", "Неверные данные!"),
    (None, "Неверные данные!"),
    ("Карта", "Неправильно введён номер карты!"),
    ("Карта ", "Неправильно введён номер карты!"),
    ("Счёт", "Неправильно введён номер счета!"),
    ("Счет ", "Неправильно введён номер счета!")
]

@pytest.mark.parametrize("state, date", card_nums)
def test_mask_account_card(state, date):
    assert mask_account_card(state) == date


@pytest.fixture
def iso_date_data():
    return [
        ("2023-10-01", "01.10.2023"),
        ("2000-01-01", "01.01.2000"),
        ("1999-12-31", "31.12.1999"),
        ("2021-07-15", "15.07.2021"),
        ("2022-02-28", "28.02.2022"),
        ("2022-12-31", "31.12.2022"),
    ]


@pytest.mark.parametrize("iso_date, expected_output", [
    ("2025-06-03T02:26:18.671407", "03.06.2025"),
])
def test_get_date(iso_date, expected_output):
    assert get_date(iso_date) == expected_output

def test_invalid_iso_date_format():
    with pytest.raises(ValueError):
        get_date("invalid-date")

def test_empty_string():
    with pytest.raises(ValueError):
        get_date("")

def test_none_input():
    with pytest.raises(TypeError):
        get_date(None)
