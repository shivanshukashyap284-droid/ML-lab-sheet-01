# Program 12: Display the first five records of a dataset using head()

import pandas as pd

def show_head(file_path):
    dataframe = pd.read_csv(file_path)
    print("First 5 records of the dataset:\n")
    print(dataframe.head())

if __name__ == "__main__":
    show_head("students.csv")
