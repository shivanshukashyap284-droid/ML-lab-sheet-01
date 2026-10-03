# Program 17: Generate descriptive statistics of numerical features

import pandas as pd

def descriptive_statistics(file_path):
    dataframe = pd.read_csv(file_path)
    print("Descriptive statistics of numerical columns:\n")
    print(dataframe.describe())

if __name__ == "__main__":
    descriptive_statistics("students.csv")
