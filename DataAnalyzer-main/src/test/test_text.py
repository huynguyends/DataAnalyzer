import pandas as pd
import unittest
import os
import sys

# append the path of the
# parent directory
if os.path.abspath(".") not in sys.path:
    sys.path.append(os.path.abspath("."))
from src.text import TextColumn


class TestTextColumn(unittest.TestCase):
    mock_csv = pd.read_csv(".\\src\\test\\text_mock_data.csv")
    actual_name = "Market"
    actual_column = mock_csv["Market"]
    actual_series = pd.Series(actual_column).astype(str)

    def test_get_name(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        output_name = textColumn.get_name()
        self.assertEqual(self.actual_name, output_name)

    def test_get_unique(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_unique = 12
        output_unique = textColumn.get_unique()
        self.assertEqual(actual_unique, output_unique)

    def test_get_missing(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_missing = 2
        output_missing = textColumn.get_missing()
        self.assertEqual(actual_missing, output_missing)

    def test_get_empty(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_empty = 2
        output_empty = textColumn.get_empty()
        self.assertEqual(actual_empty, output_empty)

    def test_get_white_space(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_whitespace = 1
        output_whitespace = textColumn.get_whitespace()
        self.assertEqual(actual_whitespace, output_whitespace)

    def test_lowercase(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_lowercase = 3
        output_lowercase = textColumn.get_lowercase()
        self.assertEqual(actual_lowercase, output_lowercase)

    def test_uppercase(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_uppercase = 1
        output_uppercase = textColumn.get_uppercase()
        self.assertEqual(actual_uppercase, output_uppercase)

    def test_alphabet(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_alphabet = 11
        output_alphabet = textColumn.get_alphabet()
        self.assertEqual(actual_alphabet, output_alphabet)

    def test_digit(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_digit = 1
        output_digit = textColumn.get_digit()
        self.assertEqual(actual_digit, output_digit)

    def test_mode(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_mode = "Central"
        output_mode = textColumn.get_mode()
        self.assertEqual(actual_mode, output_mode)

    def test_barchart(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_type = type(None)
        output_type = type(textColumn.get_barchart())
        self.assertNotEqual(actual_type, output_type)

    def test_frequent(self):
        textColumn = TextColumn(self.actual_name, self.actual_series)
        actual_type = type(None)
        output_type = type(textColumn.get_frequent())
        self.assertNotEqual(actual_type, output_type)


if __name__ == "__main__":
    unittest.main()
