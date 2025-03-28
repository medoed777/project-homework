from unittest.mock import patch, MagicMock
import pandas as pd

from src.read_csv_xlsx import read_csv_transactions, read_xlsx_transactions


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


def test_read_xlsx_success() -> None:
    with patch('pandas.read_excel') as mock_read_excel:
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{'date': '2023-01-01', 'amount': 100}]
        mock_read_excel.return_value = mock_df

        result = read_xlsx_transactions('dummy_path.xlsx')

        expected_result = [{'date': '2023-01-01', 'amount': 100}]
        assert result == expected_result

def test_read_xlsx_file_not_found() -> None:
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.side_effect = FileNotFoundError("Файл не найден")

        with patch('builtins.print') as mock_print:
            result = read_xlsx_transactions('dummy_path.xlsx')
            mock_print.assert_called_once_with("Ошибка при считывании файла: Файл не найден")
            assert result == []

def test_read_xlsx_invalid_format() -> None:
    with patch('pandas.read_excel') as mock_read_excel:
        mock_read_excel.side_effect = ValueError("Неверный формат файла")

        with patch('builtins.print') as mock_print:
            result = read_xlsx_transactions('dummy_path.xlsx')
            mock_print.assert_called_once_with("Ошибка при считывании файла: Неверный формат файла")
            assert result == []