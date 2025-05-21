import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean columns and encode outcome."""
    df.columns = df.columns.str.lower().str.strip()
    df.rename(columns={'contact': 'marketing_strategy', 'y': 'outcome'}, inplace=True)
    if df['outcome'].dtype == object:
        df['outcome'] = df['outcome'].map({'yes': 1, 'no': 0})
    return df

def encode_marketing_strategy(df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encode marketing_strategy."""
    return pd.get_dummies(df, columns=['marketing_strategy'], prefix='', prefix_sep='_')

def filter_treatment_group(df: pd.DataFrame) -> pd.DataFrame:
    """Filter treatment rows."""
    return df[df['group'] == 'treatment'].copy()

def filter_group_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Select specific columns."""
    return df[cols].copy()

def create_outcome_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Avg outcome per strategy."""
    return df.groupby('marketing_strategy')['outcome'].mean().reset_index().sort_values('outcome', ascending=False)

def convert_outcome_binary(df: pd.DataFrame) -> pd.DataFrame:
    """Map 'yes'/'no' to 1/0."""
    if df['outcome'].dtype == object:
        df['outcome'] = df['outcome'].map({'yes': 1, 'no': 0})
    return df
