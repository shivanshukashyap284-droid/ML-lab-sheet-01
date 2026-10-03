# Program 28: Add a new column to an existing dataset

import pandas as pd

def add_column(file_path):
    dataframe = pd.read_csv(file_path)
    # Add a 'Grade' column based on Marks
    dataframe["Grade"] = dataframe["Marks"].apply(
        lambda score: "A" if score >= 85 else ("B" if score >= 75 else "C")
    )
    print("Dataset after adding 'Grade' column:\n")
    print(dataframe)
    return dataframe

if __name__ == "__main__":
    add_column("students.csv")
