from unittest.mock import patch
import pandas as pd

from src.read_csv_xlsx import read_csv_transactions


def test_read_csv_success() -> None:
    with patch('pandas.read_csv') as mock_read_csv:
        mock_data = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02'],
            'amount': [100, 200],
            'description': ['Transaction 1', 'Transaction 2']
        })
        mock_read_csv.return_value = mock_data

        result = read_csv_transactions('dummy_path.csv')

        expected_result = [
            {'date': '2023-01-01', 'amount': 100, 'description': 'Transaction 1'},
            {'date': '2023-01-02', 'amount': 200, 'description': 'Transaction 2'}
        ]

        assert result == expected_result


def test_file_not_found() -> None:
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = FileNotFoundError

        result = read_csv_transactions('dummy_path.csv')

        assert result == []


def test_empty_file() -> None:
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = pd.errors.EmptyDataError

        result = read_csv_transactions('dummy_path.csv')

        assert result == []


def test_other_exception() -> None:
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = Exception("Some error")

        result = read_csv_transactions('dummy_path.csv')

        assert result == []