# Program 30: Remove duplicate records from a dataset

import pandas as pd

def remove_duplicates(file_path):
    dataframe = pd.read_csv(file_path)
    print("Number of records before removing duplicates:", len(dataframe))

    cleaned_df = dataframe.drop_duplicates()
    print("Number of records after removing duplicates:", len(cleaned_df))
    return cleaned_df

if __name__ == "__main__":
    remove_duplicates("students.csv")
