# Program 1: Install Python and verify the installed version using Python commands
# ---------------------------------------------------------------
# Installation Steps:
# 1. Download Python 3.11+ from https://www.python.org/downloads/
# 2. Run the installer and check "Add Python to PATH"
# 3. Verify installation using the command below (or 'python --version' in terminal)

import sys

def show_python_version():
    """Displays the currently installed Python version."""
    print("Python version installed:", sys.version)

if __name__ == "__main__":
    show_python_version()
