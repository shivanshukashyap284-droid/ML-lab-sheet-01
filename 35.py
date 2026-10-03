# Program 35: Generate a correlation matrix and visualize it using a heatmap

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(file_path):
    dataframe = pd.read_csv(file_path)
    numeric_df = dataframe.select_dtypes(include="number")

    correlation_matrix = numeric_df.corr()
    print("Correlation matrix:\n")
    print(correlation_matrix)

    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("correlation_heatmap.png")
    plt.show()

if __name__ == "__main__":
    correlation_heatmap("students.csv")
