
import pandas as pd
import logging

def convert_to_numeric(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Converts a column to numeric values, coercing errors to NaN.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame containing the column.
    column_name : str
        The column name to convert.

    Returns:
    -------
    pd.DataFrame
        The DataFrame with the converted column.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")

    df[column_name] = pd.to_numeric(df[column_name], errors='coerce').astype('Int64')
    logging.info(f"Converted column '{column_name}' to Int64 with NaNs handled.")

    return df