# Program 29: Delete an existing column from the dataset

import pandas as pd

def delete_column(file_path):
    dataframe = pd.read_csv(file_path)
    print("Columns before deletion:", list(dataframe.columns))

    updated_df = dataframe.drop(columns=["City"])
    print("Columns after deletion:", list(updated_df.columns))
    return updated_df

if __name__ == "__main__":
    delete_column("students.csv")
