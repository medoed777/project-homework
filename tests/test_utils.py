import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_valid_transactions() -> None:
    mock_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    m = mock_open(read_data=mock_data)

    with patch("builtins.open", m):
        with patch("os.path.isfile", return_value=True):
            transactions = load_transactions("dummy_path.json")

    assert len(transactions) == 2
    assert transactions[0]["id"] == 1
    assert transactions[1]["amount"] == 200


def test_load_invalid_json() -> None:
    m = mock_open(read_data="not a json")

    with patch("builtins.open", m):
        with patch("os.path.isfile", return_value=True):
            transactions = load_transactions("dummy_path.json")

    assert transactions == []


def test_load_empty_file() -> None:
    m = mock_open(read_data="")

    with patch("builtins.open", m):
        with patch("os.path.isfile", return_value=True):
            transactions = load_transactions("dummy_path.json")

    assert transactions == []


def test_load_non_existent_file() -> None:
    with patch("os.path.isfile", return_value=False):
        transactions = load_transactions("dummy_path.json")

    assert transactions == []


def test_load_io_error() -> None:
    m = mock_open()

    with patch("builtins.open", m):
        m.side_effect = IOError("File not accessible")
        with patch("os.path.isfile", return_value=True):
            transactions = load_transactions("dummy_path.json")

    assert transactions == []
