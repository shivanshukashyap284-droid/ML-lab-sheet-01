# Program 5: Install Matplotlib and create a simple line plot
# ---------------------------------------------------------------
# Installation: pip install matplotlib

import matplotlib
import matplotlib.pyplot as plt

def create_line_plot():
    print("Matplotlib version:", matplotlib.__version__)
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 4, 6, 8, 10]

    plt.plot(x_values, y_values, marker="o", color="blue")
    plt.title("Simple Line Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.savefig("line_plot.png")
    plt.show()

if __name__ == "__main__":
    create_line_plot()
