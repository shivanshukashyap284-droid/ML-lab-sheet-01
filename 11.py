# Program 11: Load a CSV dataset using the Pandas library

import pandas as pd

def load_dataset(file_path):
    try:
        dataframe = pd.read_csv(file_path)
        print("Dataset loaded successfully!\n")
        print(dataframe)
        return dataframe
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    load_dataset("students.csv")
