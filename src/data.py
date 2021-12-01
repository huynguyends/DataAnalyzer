import streamlit as st
from dataclasses import dataclass
import pandas as pd


@dataclass
class Dataset:
    name: str
    df: pd.DataFrame

    def get_name(self):
        """
        Return filename of loaded dataset
        """
        return self.name

    def get_n_rows(self):
        """
        Return number of rows of loaded dataset
        """
        return self.df.shape[0]

    def get_n_cols(self):
        """
        Return number of columns of loaded dataset
        """
        return self.df.shape[1]

    def get_cols_list(self):
        """
        Return list column names of loaded dataset
        """
        return self.df.columns.to_list()

    def get_cols_dtype(self):
        """
        Return dictionary with column name as keys and data type as values
        """
        return self.df.dtypes.apply(lambda x: x.name).to_dict()  # convert to dataframe by using from_dict() later

    def get_n_duplicates(self):
        """
        Return number of duplicated rows of loaded dataset
        """

        return self.df.duplicated().sum()

    def get_n_missing(self):
        """
        Return number of rows with missing values of loaded dataset
        """
        return (
            self.df.isnull().any(axis=1).sum()
        )  # return dataframe of booleans if rows have a missing value, then sum it up

    def get_head(self, n=5):
        """
        Return Pandas Dataframe with top rows of loaded dataset
        """
        return self.df.head(n)

    def get_tail(self, n=5):
        """
        Return Pandas Dataframe with bottom rows of loaded dataset
        """
        return self.df.tail(n)

    def get_sample(self, n=5):
        """
        Return Pandas Dataframe with random sampled rows of loaded dataset
        """
        return self.df.sample(n)

    def get_numeric_columns(self):
        """
        Return list column names of numeric type from loaded dataset
        """
        num_cols_list = [
            col
            for col, type in self.get_cols_dtype().items()
            if type in ["int16", "int32", "int64", "float16", "float32", "float64"]
        ]  # if type of column in columns list is a nummeric type, include in list
        return num_cols_list

    def get_text_columns(self):
        """
        Return list column names of text type from loaded dataset
        """
        text_cols_list = [
            col for col, type in self.get_cols_dtype().items() if type == "object"
        ]  # if type of column in columns list is an object (string) type, include in list
        return text_cols_list

    def get_date_columns(self):
        """
        Return list column names of datetime type from loaded dataset
        """
        date_list = self.df.select_dtypes(include= ['datetime','datetimetz'])


        return date_list.columns.tolist()
