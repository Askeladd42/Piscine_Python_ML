import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file and return a pandas DataFrame."""
    try:
        # Load the CSV file
        data = pd.read_csv(path)

        # Print the dimensions of the dataset
        print(f"Loading dataset of dimensions {data.shape}")

        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
