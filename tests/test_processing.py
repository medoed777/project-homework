from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "PENDING", "amount": 200},
        {"id": 3, "state": "EXECUTED", "amount": 300},
        {"id": 4, "state": "CANCELED", "amount": 400},
        {"id": 5, "state": "EXECUTED", "amount": 500},
    ]


@pytest.mark.parametrize(
    "state, expected_output",
    [
        (
            "EXECUTED",
            [
                {"id": 1, "state": "EXECUTED", "amount": 100},
                {"id": 3, "state": "EXECUTED", "amount": 300},
                {"id": 5, "state": "EXECUTED", "amount": 500},
            ],
        ),
        (
            "PENDING",
            [
                {"id": 2, "state": "PENDING", "amount": 200},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 4, "state": "CANCELED", "amount": 400},
            ],
        ),
        ("INVALID_STATE", []),  # Проверка на несуществующее состояние
    ],
)
def test_filter_by_state(sample_data: List[Dict[str, Any]], state: str, expected_output: List[Dict[str, Any]]) -> None:
    assert filter_by_state(sample_data, state) == expected_output


def test_empty_list() -> None:
    assert filter_by_state([], "EXECUTED") == []


def sample_data_list() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "reverse, expected_order",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(reverse: bool, expected_order: List[Dict[str, Any]]) -> None:
    sample_data = sample_data_list()
    sorted_data = sort_by_date(sample_data, reverse)
    assert sorted_data == expected_order


def test_empty_list_date() -> None:
    assert sort_by_date([]) == []
