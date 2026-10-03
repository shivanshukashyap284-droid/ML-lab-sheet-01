# Program 18: Display complete information about the dataset using info()

import pandas as pd

def dataset_info(file_path):
    dataframe = pd.read_csv(file_path)
    print("Complete dataset information:\n")
    dataframe.info()

if __name__ == "__main__":
    dataset_info("students.csv")
