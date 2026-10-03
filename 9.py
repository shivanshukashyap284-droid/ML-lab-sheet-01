# Program 9: Create and execute a Python script using Visual Studio Code or PyCharm
# ---------------------------------------------------------------
# This script can be run using: python 9.py

def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}! This script runs outside Jupyter (VS Code / PyCharm)."

if __name__ == "__main__":
    message = greet("Student")
    print(message)
