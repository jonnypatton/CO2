import pandas as pd
import logging

def convert_to_datetime(df: pd.DataFrame, column_name: str, timezone: str = "Europe/London") -> pd.DataFrame:
    """
    Converts a column to datetime format and ensures proper timezone conversion.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame containing the column.
    column_name : str
        The column name to convert.
    timezone : str, optional
        The timezone to convert to (default: 'Europe/London').

    Returns:
    -------
    pd.DataFrame
        The DataFrame with the datetime column converted and timezone-adjusted.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")

    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')

    # Ensure timezone is properly set
    if df[column_name].dt.tz is None:
        df[column_name] = df[column_name].dt.tz_localize('UTC', ambiguous='NaT')

    df[column_name] = df[column_name].dt.tz_convert(timezone)
    logging.info(f"Converted column '{column_name}' to datetime with timezone: {timezone}")

    return df