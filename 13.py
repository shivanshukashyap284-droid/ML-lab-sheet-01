# Program 13: Display the last five records of a dataset using tail()

import pandas as pd

def show_tail(file_path):
    dataframe = pd.read_csv(file_path)
    print("Last 5 records of the dataset:\n")
    print(dataframe.tail())

if __name__ == "__main__":
    show_tail("students.csv")
