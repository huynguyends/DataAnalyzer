# To be filled by students
from dataclasses import dataclass
import streamlit as st
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import pandas as pd


@dataclass
class NumericColumn:
    col_name: str
    series: pd.Series

    def __init__(self, col_name, series):
        self.col_name = col_name
        self.series = series

    def get_name(self):
        """
        Return name of selected column
        """
        return self.col_name

    def get_unique(self):
        """
        Return number of unique values for selected column
        """
        len_unique_value_column = len(pd.unique(self.series))
        return len_unique_value_column

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        a = self.series.isna().sum()
        return a

    def get_zeros(self):
        """
        Return number of occurrence of 0 value for selected column
        """
        b = 0
        for i in range(self.series.size):
            if self.series[i] == 0:
                b = b + 1
        return b

    def get_negatives(self):
        """
        Return number of negative values for selected column
        """
        c = 0
        for i in range(self.series.size):
            if self.series[i] < 0:
                c = c + 1
        return c

    def get_mean(self):
        """
        Return the average value for selected column
        """
        mean_value = self.series.mean()
        return mean_value

    def get_std(self):
        """
        Return the standard deviation value for selected column
        """
        standard_deviation = self.series.std()
        return standard_deviation

    def get_min(self):
        """
        Return the minimum value for selected column
        """
        min_value = self.series.min()
        return min_value

    def get_max(self):
        """
        Return the maximum value for selected column
        """
        max_value = self.series.max()
        return max_value

    def get_median(self):
        """
        Return the median value for selected column
        """
        median_value = self.series.median()
        return median_value

    def get_histogram(self):
        """
        Return the generated histogram for selected column
        """
        column_numeric = self.series
        column_numeric.hist(bins=50)
        st.set_option("deprecation.showPyplotGlobalUse", False)
        histogram = st.pyplot()
        return histogram

    def get_frequent(self):
        """
        Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
        """
        column_bar = pd.DataFrame(self.series.value_counts(sort=True, ascending=False, dropna=True))
        column_bar.columns = ["values_count"]
        percentage_count = pd.DataFrame(
            self.series.value_counts(normalize=True, sort=True, ascending=False, dropna=True)
        )
        column_bar["percentage"] = percentage_count
        return column_bar.head(20)
