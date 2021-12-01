import streamlit as st
import pandas as pd
import sys
import os

if os.path.abspath(".") not in sys.path:
    sys.path.append(os.path.abspath("."))
from src.text import TextColumn
from src.numeric import NumericColumn
from src.data import Dataset


def streamlit_overall(name, df):
    """
    Uses Functions from class Dataset and returns values to main()
    Args:
        name [str] : uploaded file name
        df [pd.Dataframe]: dataframe of uploaded file

    """
    dataset = Dataset(name, df)
    st.write(f"__Name of Table:__ {dataset.get_name()}")
    rows_number = dataset.get_n_rows()
    st.write(f"__Number of Rows:__ {rows_number}")
    st.write(f"__Number of Columns:__ {dataset.get_n_cols()}")
    st.write(f"__Number of Duplicated Rows:__ {dataset.get_n_duplicates()}")
    st.write(f"__Number of Missing Values:__ \n{dataset.get_n_missing()}")
    st.write(f"__List of Columns:__ {dataset.get_cols_list()}")
    option = st.selectbox(
        "Which column do you want to convert to dates?",
        ["None"] + dataset.get_text_columns(),
    )
    if option != "None":
        try:
            dataset.df[option] = pd.to_datetime(dataset.df[option])
        except:
            None
    df_dict = dataset.get_cols_dtype()
    df = pd.DataFrame(list(df_dict.items()), columns=["Column Name", "Data-Type"])
    st.subheader(f"__Type of Columns:__ ")
    st.dataframe(df)
    x = st.slider("select the number of the rows to be displayed", min_value=5, max_value=rows_number, step=1)
    st.write("__Top Rows of Table__")
    st.write(dataset.get_head(x))
    st.write("__Bottom Rows of Table__")
    st.write(dataset.get_tail(x))
    st.write("__Random Sample Rows of Table__")
    st.write(dataset.get_sample(x))
    st.write(f"__Numeric columns of Table:__ {dataset.get_numeric_columns()}")
    st.write(f"__Text columns of Table:__ {dataset.get_text_columns()}")
    st.write(f"__Date columns of Table:__ {dataset.get_date_columns()}")


def streamlit_text(name, df):
    """Uses Functions from class TextColumn and returns values to main()

    Args:
        name [str] : uploaded file name
        df [pd.Dataframe]: dataframe of uploaded file

    """
    datasetobj1 = Dataset(name, df)
    list_text_columns = datasetobj1.get_text_columns()
    text_columns = df[list_text_columns].astype(str)
    j = 3.0
    for value in text_columns:
        series = pd.Series(text_columns[value])

        textColumn = TextColumn(value, series)
        st.subheader(f"__{round(j,1)} Field Name: _{textColumn.get_name()}___")
        col1, col2 = st.columns(2)
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Unique Values" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_unique()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Missing Values" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_missing()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Empty Rows" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_empty()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Rows with Whitespace" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_whitespace()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Rows with only Lowercases" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_lowercase()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Rows with only Uppercases" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_uppercase()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Rows with only alphabet" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_alphabet()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Rows with only Numbers" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{textColumn.get_digit()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Mode value" + "</p>", unsafe_allow_html=True
        )
        col2.write(f"__{textColumn.get_mode()}__")
        st.write("__Bar Chart__")
        textColumn.get_barchart()
        st.subheader("__Most Frequent Value__")
        st.write(textColumn.get_frequent())
        j = j + 0.1


def streamlit_numeric(name, df):
    """Uses Functions from class NumericColumn and returns values to main()

    Args:
        name [str] : uploaded file name
        df [pd.Dataframe]: dataframe of uploaded file

    """
    datasetobj2 = Dataset(name, df)
    list_numeric_columns = datasetobj2.get_numeric_columns()
    numeric_columns = df[list_numeric_columns]

    i = 2.0
    for value in numeric_columns:
        series = pd.Series(numeric_columns[value])

        numericColumn = NumericColumn(value, series)
        st.subheader(f"__{round(i,1)} Field Name: _{numericColumn.get_name()}___")
        col1, col2 = st.columns(2)
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Unique Values" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{numericColumn.get_unique()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Missing Values" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{numericColumn.get_missing()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Rows with 0" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{numericColumn.get_zeros()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Number of Rows with Negative Values" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{numericColumn.get_negatives()}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Average Value" + "</p>", unsafe_allow_html=True
        )
        col2.write(f"__{round(numericColumn.get_mean(), 4)}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "St andard Deviation Value" + "</p>",
            unsafe_allow_html=True,
        )
        col2.write(f"__{round(numericColumn.get_std(), 4)}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Minimum Value" + "</p>", unsafe_allow_html=True
        )
        col2.write(f"__{round(numericColumn.get_min(), 4)}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Maximum Value" + "</p>", unsafe_allow_html=True
        )
        col2.write(f"__{round(numericColumn.get_max(), 4)}__")
        col1.markdown(
            "<p style='text-align:right;background-color:AliceBlue'>" + "Median Value" + "</p>", unsafe_allow_html=True
        )
        col2.write(f"__{round(numericColumn.get_median(), 4)}__")
        i = i + 0.1
        st.write("__Histogram__")
        numericColumn.get_histogram()
        st.subheader("__Most Frequent Value__")
        st.write(numericColumn.get_frequent())


def main():
    st.title("Data Explorer Tool")
    try:
        uploaded_file = st.file_uploader("Choose a csv file", type=["csv"])

        if uploaded_file is None:
            return None
        else:
            df = pd.read_csv(uploaded_file)
            # df = df.apply(lambda col: pd.to_datetime(col, errors="ignore") if col.dtypes == object else col, axis=0)
            st.header("1. Overall Information of the dataset")
            try:
                streamlit_overall(uploaded_file.name, df)
            except:
                st.error("Error in Overall Function")
            st.header("2. Information on numeric columns")
            try:
                streamlit_numeric(uploaded_file.name, df)
            except:
                st.error("Error in Numeric Function")
            st.header("3. Information on text columns")
            try:
                streamlit_text(uploaded_file.name, df)
            except:
                st.error("Error in Text Function")
            st.caption("created by _Huy_, _Simon_ & _Chitvan_")
    except:
        st.error("Error in Uploaded CSV")


if __name__ == "__main__":
    main()
