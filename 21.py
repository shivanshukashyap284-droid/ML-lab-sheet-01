# Program 21: Display unique values present in a selected column

import pandas as pd

def show_unique_values(file_path, column_name):
    dataframe = pd.read_csv(file_path)
    print(f"Unique values in '{column_name}' column:")
    print(dataframe[column_name].unique())

if __name__ == "__main__":
    show_unique_values("students.csv", "City")
