# Program 26: Filter records based on a given condition

import pandas as pd

def filter_records(file_path):
    dataframe = pd.read_csv(file_path)
    # Filter students who scored more than 80 marks
    filtered_data = dataframe[dataframe["Marks"] > 80]
    print("Students who scored more than 80 marks:\n")
    print(filtered_data)

if __name__ == "__main__":
    filter_records("students.csv")
