# Program 24: Select specific rows and columns using loc[]

import pandas as pd

def select_with_loc(file_path):
    dataframe = pd.read_csv(file_path)
    # Select rows 0 to 3 and only 'Name' and 'Marks' columns
    selected_data = dataframe.loc[0:3, ["Name", "Marks"]]
    print("Selected data using loc[]:\n")
    print(selected_data)

if __name__ == "__main__":
    select_with_loc("students.csv")
