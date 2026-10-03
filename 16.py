# Program 16: Check the data types of all columns

import pandas as pd

def check_data_types(file_path):
    dataframe = pd.read_csv(file_path)
    print("Data types of each column:\n")
    print(dataframe.dtypes)

if __name__ == "__main__":
    check_data_types("students.csv")
