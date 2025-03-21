from typing import Any
from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import conversion_currency


@pytest.fixture
def mock_requests_get() -> Any:
    with patch("requests.get") as mock:
        yield mock


def test_conversion_rub(mock_requests_get: Mock) -> None:
    transactions = {"amount": 100, "currency": "RUB"}
    result = conversion_currency(transactions)

    assert result == 100
    mock_requests_get.assert_not_called()


def test_conversion_http_error(mock_requests_get: Mock) -> None:
    mock_requests_get.side_effect = requests.exceptions.HTTPError("HTTP error occurred")

    transactions = {"amount": 100, "currency": "USD"}
    result = conversion_currency(transactions)

    assert result is None
    mock_requests_get.assert_called_once()


def test_conversion_no_result(mock_requests_get: Mock) -> None:
    mock_response = Mock()

    mock_response.json.return_value = {}
    mock_response.raise_for_status = Mock()
    mock_requests_get.return_value = mock_response

    transactions = {"amount": 100, "currency": "USD"}
    result = conversion_currency(transactions)

    assert result is None
    mock_requests_get.assert_called_once()
