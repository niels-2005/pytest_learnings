import pytest
import pandas as pd


def read_data():
    return pd.read_csv("./data.csv")


# Case 1
@pytest.mark.parametrize(
    "row_index, expected_name, expected_age",
    [
        (0, "Alice", 30),
        (1, "Bob", 25),
        (2, "Charlie", 35),
    ],
)
def test_read_data_row(row_index, expected_name, expected_age):
    # read dataframe and check
    df = read_data()
    assert df.loc[row_index, "name"] == expected_name
    assert df.loc[row_index, "age"] == expected_age


# Case 2
@pytest.mark.parametrize(
    "file_path, expected_rows",
    [
        ("./data1.csv", 3),
        ("./data2.csv", 5),
        ("./data3.csv", 0),
    ],
)
def test_read_data_shape(file_path, expected_rows):
    df = pd.read_csv(file_path)
    assert len(df) == expected_rows


# Case 3
# Fixture: wird nur einmal ausgeführt (je nach Scope)
@pytest.fixture(scope="module")
def df():
    return pd.read_csv("./data.csv")


# Parametrisierter Test, der das geladene DataFrame verwendet
@pytest.mark.parametrize(
    "row_index, expected_name, expected_age",
    [
        (0, "Alice", 30),
        (1, "Bob", 25),
        (2, "Charlie", 35),
    ],
)
def test_read_data_rows(df, row_index, expected_name, expected_age):
    assert df.loc[row_index, "name"] == expected_name
    assert df.loc[row_index, "age"] == expected_age
