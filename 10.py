# Program 10: Create a virtual environment and install required Python libraries inside it
# ---------------------------------------------------------------
# Steps to create and use a virtual environment (run in terminal):
#   python -m venv ml_env
#   ml_env\Scripts\activate        (Windows)
#   source ml_env/bin/activate     (Linux / Mac)
#   pip install numpy pandas matplotlib seaborn scikit-learn

import sys

def check_environment():
    """Prints the Python executable path currently in use."""
    print("Python executable in use:", sys.executable)
    print("If this path points inside the 'ml_env' folder, the virtual environment is active.")

if __name__ == "__main__":
    check_environment()
