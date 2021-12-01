import pandas as pd
import unittest
import os
import sys

# append the path of the parent directory
if os.path.abspath(".") not in sys.path:
    sys.path.append(os.path.abspath("."))
from src.numeric import NumericColumn


class TestNumericColumn(unittest.TestCase):
    mock = pd.read_csv(".\\src\\test\\numeric_mock_data.csv")
    actual_name = "Inventory"
    actual_column = mock["Inventory"]
    actual_series = pd.Series(actual_column)

    def test_get_name(self):
        """ 
        test column name is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_name = numericColumn.get_name()
        self.assertEqual(self.actual_name, output_name)

    def test_get_unique_values(self):
        """" 
        test number of unique value is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_unique = numericColumn.get_unique()
        actual_unique = 13
        self.assertEqual(actual_unique, output_unique)

    def test_get_missing(self):
        """
        test number of missing data is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_missing = numericColumn.get_missing()
        actual_missing = 2
        self.assertEqual(actual_missing, output_missing)

    def test_get_zeros(self):
        """
        test number of zero value is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_zeros = numericColumn.get_zeros()
        actual_zeros = 2
        self.assertEqual(actual_zeros, output_zeros)

    def test_get_negatives(self):
        """
        test number of negatives is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_negatives = numericColumn.get_negatives()
        actual_negatives = 2
        self.assertEqual(actual_negatives, output_negatives)

    def test_get_mean(self):
        """
        test mean valuse is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_mean = numericColumn.get_mean()
        actual_mean = 371.57142857142856
        self.assertEqual(actual_mean, output_mean)

    def test_get_std(self):
        """
        test stardard deviation value is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_std = numericColumn.get_std()
        actual_std = 525.5044044733394
        self.assertEqual(actual_std, output_std)

    def test_get_min(self):
        """
        test min value is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_min = numericColumn.get_min()
        actual_min = -762
        self.assertEqual(actual_min, output_min)

    def test_get_max(self):
        """
        test max value is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_max = numericColumn.get_max()
        actual_max = 1000
        self.assertEqual(actual_max, output_max)

    def test_get_median(self):
        """
        test median value is equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_median = numericColumn.get_median()
        actual_median = 390
        self.assertEqual(actual_median, output_median)

    def test_get_histogram(self):
        """
        test type in histogram is not equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_type = type(numericColumn.get_histogram())
        actual_type = type(None)
        self.assertNotEqual(actual_type, output_type)

    def test_get_frequent(self):
        """
        test type in freqquent is not equal between test and actual
        """
        numericColumn = NumericColumn(self.actual_name, self.actual_series)
        output_type = type(numericColumn.get_frequent())
        actual_type = type(None)
        self.assertNotEqual(actual_type, output_type)


if __name__ == "__main__":
    unittest.main()
