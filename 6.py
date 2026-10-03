# Program 6: Install Seaborn and generate a basic statistical plot
# ---------------------------------------------------------------
# Installation: pip install seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def create_seaborn_plot():
    print("Seaborn version:", sns.__version__)
    np.random.seed(42)
    sample_data = np.random.normal(loc=50, scale=10, size=200)

    sns.histplot(sample_data, kde=True, color="skyblue")
    plt.title("Basic Statistical Plot using Seaborn")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("seaborn_plot.png")
    plt.show()

if __name__ == "__main__":
    create_seaborn_plot()
