# Program 32: Load a dataset directly from the Scikit-learn library

from sklearn.datasets import load_iris
import pandas as pd

def load_sklearn_dataset():
    iris_data = load_iris()
    dataframe = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    dataframe["target"] = iris_data.target

    print("Iris dataset loaded from Scikit-learn:\n")
    print(dataframe.head())
    return dataframe

if __name__ == "__main__":
    load_sklearn_dataset()
