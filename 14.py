# Program 14: Find the total number of rows and columns in a dataset

import pandas as pd

def dataset_shape(file_path):
    dataframe = pd.read_csv(file_path)
    rows, columns = dataframe.shape
    print(f"Number of rows: {rows}")
    print(f"Number of columns: {columns}")

if __name__ == "__main__":
    dataset_shape("students.csv")
