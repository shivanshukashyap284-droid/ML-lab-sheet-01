# Program 25: Select specific rows and columns using iloc[]

import pandas as pd

def select_with_iloc(file_path):
    dataframe = pd.read_csv(file_path)
    # Select first 3 rows and first 2 columns by position
    selected_data = dataframe.iloc[0:3, 0:2]
    print("Selected data using iloc[]:\n")
    print(selected_data)

if __name__ == "__main__":
    select_with_iloc("students.csv")
