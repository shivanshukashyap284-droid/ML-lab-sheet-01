# Program 20: Count the total missing values in each column

import pandas as pd

def count_missing_values(file_path):
    dataframe = pd.read_csv(file_path)
    print("Total missing values in each column:\n")
    print(dataframe.isnull().sum())

if __name__ == "__main__":
    count_missing_values("students.csv")
