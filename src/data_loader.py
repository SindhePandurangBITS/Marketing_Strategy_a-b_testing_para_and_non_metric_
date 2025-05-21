import pandas as pd
import os

def load_bank_data(path: str) -> pd.DataFrame:
    """
    Load the Bank Marketing dataset from a CSV file.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found at: {path}")
    
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower().str.strip()  # clean column names
    return df
