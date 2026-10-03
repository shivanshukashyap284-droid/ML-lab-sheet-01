# Program 22: Count the frequency of each unique value in a column

import pandas as pd

def value_frequency(file_path, column_name):
    dataframe = pd.read_csv(file_path)
    print(f"Frequency of each unique value in '{column_name}' column:\n")
    print(dataframe[column_name].value_counts())

if __name__ == "__main__":
    value_frequency("students.csv", "City")
