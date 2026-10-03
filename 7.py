# Program 7: Install Scikit-learn and verify its version
# ---------------------------------------------------------------
# Installation: pip install scikit-learn

import sklearn

def verify_sklearn():
    print("Scikit-learn version:", sklearn.__version__)

if __name__ == "__main__":
    verify_sklearn()
