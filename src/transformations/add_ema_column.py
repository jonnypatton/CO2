import logging

import pandas as pd


def add_ema_column(df: pd.DataFrame, column_name: str = 'state', ema_span: int = 15) -> pd.DataFrame:
    """
    Adds an Exponential Moving Average (EMA) column to the DataFrame and forces it to an integer format.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column_name : str, optional
        The column to compute the EMA on (default: 'state').
    ema_span : int, optional
        The span for the EMA calculation (default: 15).

    Returns:
    -------
    pd.DataFrame
        The DataFrame with the new EMA column added as Int64.

    Raises:
    ------
    ValueError:
        If the specified column does not exist in the DataFrame.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")

    ema_column_name = f"{ema_span}_point_ema"

    df[ema_column_name] = df[column_name].ewm(span=ema_span, adjust=False).mean()

    df[ema_column_name] = df[ema_column_name].round().astype('Int64')

    logging.info(f"Added EMA column '{ema_column_name}' with span={ema_span} as Int64 based on '{column_name}'.")

    return df