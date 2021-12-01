import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class TextColumn:
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
        a = 0
        for i in range(self.series.size):
            if self.series[i] == "nan" or self.series[i] == "NaN":
                a = a + 1
        return a

    def get_empty(self):
        """
        Return number of rows with empty string for selected column
        """
        b = 0
        for i in range(self.series.size):
            if self.series[i].replace(" ", "") == '""' or self.series[i].replace(" ", "") == "''":
                b = b + 1
        return b

    def get_whitespace(self):
        """
        Return number of rows with only whitespaces for selected column
        """
        c = 0
        for i in range(self.series.size):
            if type(self.series[i]) == type(None) or type(self.series[i]) == type(0):
                continue
            check_white_space = self.series[i].isspace()
            if check_white_space == True:
                c = c + 1
        return c

    def get_lowercase(self):
        """
        Return number of rows with only lower case characters for selected column
        """
        d = 0
        for i in range(self.series.size):
            if type(self.series[i]) == type(None) or type(self.series[i]) == type(0):
                continue
            check_lower = self.series[i].islower()
            if check_lower == True:
                d = d + 1
        return d

    def get_uppercase(self):
        """
        Return number of rows with only upper case characters for selected column
        """
        e = 0
        for i in range(self.series.size):
            if type(self.series[i]) == type(None) or type(self.series[i]) == type(0):
                continue
            check_upper = self.series[i].isupper()
            if check_upper == True:
                e = e + 1
        return e

    def get_alphabet(self):
        """
        Return number of rows with only alphabet characters for selected column
        """
        f = 0
        for i in range(self.series.size):
            if type(self.series[i]) == type(None) or type(self.series[i]) == type(0):
                continue
            check_alpha = self.series[i].isalpha()
            if check_alpha == True:
                f = f + 1
        return f

    def get_digit(self):
        """
        Return number of rows with only numbers as characters for selected column
        """
        g = 0
        for i in range(self.series.size):
            if type(self.series[i]) == type(None):
                continue
            check_numeric = self.series[i].isnumeric()
            if check_numeric == True:
                g = g + 1
        return g

    def get_mode(self):
        """
        Return the mode value for selected column
        """
        h = self.series.mode()
        return h[0]

    def get_barchart(self):
        """
        Return the generated bar chart for selected column
        """
        column_bar = pd.DataFrame(self.series.value_counts(sort=True, ascending=False, dropna=True))
        column_bar.columns = ["values_count"]
        bar_plot = st.bar_chart(data=column_bar, width=5, height=200, use_container_width=True)

        return bar_plot

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
