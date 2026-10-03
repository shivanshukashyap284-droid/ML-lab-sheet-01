# Program 15: Display the names of all columns in the dataset

import pandas as pd

def show_column_names(file_path):
    dataframe = pd.read_csv(file_path)
    print("Column names in the dataset:")
    print(list(dataframe.columns))

if __name__ == "__main__":
    show_column_names("students.csv")
