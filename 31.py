# Program 31: Save the modified dataset as a new CSV file

import pandas as pd

def save_modified_dataset(file_path, output_path):
    dataframe = pd.read_csv(file_path)
    # Example modification: remove duplicates before saving
    cleaned_df = dataframe.drop_duplicates()
    cleaned_df.to_csv(output_path, index=False)
    print(f"Modified dataset saved successfully as '{output_path}'")

if __name__ == "__main__":
    save_modified_dataset("students.csv", "students_modified.csv")
