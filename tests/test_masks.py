from typing import List, Optional, Tuple

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def test_card_numbers() -> List[Tuple[Optional[str], str]]:
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("4111111111111111", "4111 11** **** 1111"),
        ("0000000000000000", "0000 00** **** 0000"),
        (" 1234567812345678 ", "1234 56** **** 5678"),
        (None, "Неправильно введён номер карты!"),
    ]


@pytest.mark.parametrize(
    "input_card, expected_output",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("4111111111111111", "4111 11** **** 1111"),
        ("0000000000000000", "0000 00** **** 0000"),
        (" 1234567812345678 ", "1234 56** **** 5678"),
        (None, "Неправильно введён номер карты!"),
    ],
)
def test_masking_standard_card_number(input_card: Optional[str], expected_output: str) -> None:
    result = get_mask_card_number(input_card)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_card, expected_output",
    [
        ("1234", "Неправильно введён номер карты!"),
        ("", "Неправильно введён номер карты!"),
        ("abcd", "Неправильно введён номер карты!"),
        ("1234abcd", "Неправильно введён номер карты!"),
        ("12345678901234567890", "Неправильно введён номер карты!"),
        (None, "Неправильно введён номер карты!"),
    ],
)
def test_masking_invalid_input(input_card: Optional[str], expected_output: str) -> None:
    result = get_mask_card_number(input_card)
    assert result == expected_output


@pytest.fixture
def valid_cash_numbers() -> List[str]:
    return [
        "1234567890",
        "9876543210",
    ]


def test_get_mask_account_valid(valid_cash_numbers: List[str]) -> None:
    for cash_number in valid_cash_numbers:
        result = get_mask_account(cash_number)
        assert result == "**" + cash_number[-4:]


@pytest.fixture
def invalid_cash_numbers_too_short() -> List[str]:
    return [
        "12345",
        "123456",
    ]


def test_get_mask_account_too_short(invalid_cash_numbers_too_short: List[str]) -> None:
    for cash_number in invalid_cash_numbers_too_short:
        result = get_mask_account(cash_number)
        assert result == "Неправильно введён номер счета!"


@pytest.fixture
def invalid_cash_numbers_not_digits() -> List[str]:
    return [
        "123456A890",
        "A1234567890",
        "1234-567890",
    ]


def test_get_mask_account_not_digits(invalid_cash_numbers_not_digits: List[str]) -> None:
    for cash_number in invalid_cash_numbers_not_digits:
        result = get_mask_account(cash_number)
        assert result == "Неправильно введён номер счета!"


@pytest.fixture
def invalid_cash_numbers_none() -> List[Optional[str]]:
    return [None, ""]


def test_get_mask_account_none(invalid_cash_numbers_none: List[Optional[str]]) -> None:
    for cash_number in invalid_cash_numbers_none:
        result = get_mask_account(cash_number)
        assert result == "Неправильно введён номер счета!"
