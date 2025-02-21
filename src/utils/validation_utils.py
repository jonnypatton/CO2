import pandas as pd
import logging
from typing import NoReturn

def validate_no_nans(df: pd.DataFrame) -> NoReturn:
    """
    Validates that the DataFrame contains no NaN values. If NaNs are found, logs an error and raises an exception.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame to validate.

    Raises:
    ------
    ValueError:
        If the DataFrame contains NaN values.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    nan_counts = df.isna().sum()

    nan_report = {col: count for col, count in nan_counts.items() if count > 0}

    if nan_report:
        logging.error(f"Validation failed: Data contains NaN values in columns: {nan_report}")
        raise ValueError(f"Data contains NaNs in columns: {nan_report}")