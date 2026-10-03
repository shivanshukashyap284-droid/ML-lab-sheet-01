# Program 3: Install NumPy using pip and verify its installation
# ---------------------------------------------------------------
# Installation: pip install numpy

import numpy as np

def verify_numpy():
    print("NumPy version:", np.__version__)
    sample_array = np.array([1, 2, 3, 4, 5])
    print("Sample NumPy array:", sample_array)

if __name__ == "__main__":
    verify_numpy()
