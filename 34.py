# Program 34: Create a scatter plot to visualize the relationship between two variables

import pandas as pd
import matplotlib.pyplot as plt

def create_scatter_plot(file_path):
    dataframe = pd.read_csv(file_path)
    plt.scatter(dataframe["Age"], dataframe["Marks"], color="purple")
    plt.title("Scatter Plot: Age vs Marks")
    plt.xlabel("Age")
    plt.ylabel("Marks")
    plt.savefig("scatter_plot.png")
    plt.show()

if __name__ == "__main__":
    create_scatter_plot("students.csv")
