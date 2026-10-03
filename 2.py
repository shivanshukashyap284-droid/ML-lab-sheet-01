# Program 2: Install Jupyter Notebook and launch the notebook interface
# ---------------------------------------------------------------
# Installation: pip install notebook
# Launch:       jupyter notebook   (run in terminal)

import subprocess

def check_jupyter_installed():
    """Checks whether Jupyter is installed and prints its version."""
    try:
        result = subprocess.run(["jupyter", "--version"], capture_output=True, text=True)
        print("Jupyter installation details:\n", result.stdout)
    except FileNotFoundError:
        print("Jupyter not found. Install it using: pip install notebook")

if __name__ == "__main__":
    check_jupyter_installed()
