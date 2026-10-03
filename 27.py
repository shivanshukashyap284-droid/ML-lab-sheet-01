# Program 27: Sort the dataset using one or more columns

import pandas as pd

def sort_dataset(file_path):
    dataframe = pd.read_csv(file_path)
    sorted_data = dataframe.sort_values(by=["Marks"], ascending=False)
    print("Dataset sorted by Marks (descending):\n")
    print(sorted_data)

if __name__ == "__main__":
    sort_dataset("students.csv")
