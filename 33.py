# Program 33: Create a histogram for a numerical feature using Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

def create_histogram(file_path):
    dataframe = pd.read_csv(file_path)
    plt.hist(dataframe["Marks"].dropna(), bins=5, color="teal", edgecolor="black")
    plt.title("Histogram of Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("histogram_marks.png")
    plt.show()

if __name__ == "__main__":
    create_histogram("students.csv")
