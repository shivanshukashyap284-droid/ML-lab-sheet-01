# Program 4: Install Pandas using pip and verify its installation
# ---------------------------------------------------------------
# Installation: pip install pandas

import pandas as pd

def verify_pandas():
    print("Pandas version:", pd.__version__)
    sample_df = pd.DataFrame({"Column_A": [1, 2, 3]})
    print("Sample DataFrame:\n", sample_df)

if __name__ == "__main__":
    verify_pandas()
