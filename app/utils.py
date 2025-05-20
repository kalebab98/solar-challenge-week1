import pandas as pd
import os

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the file.
    """
    try:
        # Check if the file exists before trying to load it
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            return df
        else:
            raise FileNotFoundError(f"File {file_path} does not exist.")
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {str(e)}")
