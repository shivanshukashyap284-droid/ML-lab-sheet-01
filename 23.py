# Program 23: Rename one or more columns in a dataset

import pandas as pd

def rename_columns(file_path):
    dataframe = pd.read_csv(file_path)
    print("Columns before renaming:", list(dataframe.columns))

    renamed_df = dataframe.rename(columns={"Marks": "Score", "City": "Location"})
    print("Columns after renaming:", list(renamed_df.columns))
    return renamed_df

if __name__ == "__main__":
    rename_columns("students.csv")
