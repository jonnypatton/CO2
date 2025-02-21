import logging

import pandas as pd

from src.utils.validation_utils import validate_no_nans


def fill_nans_with_mean(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Fill NaN values in a specified column by interpolating the mean
    of the nearest non-NaN values before and after. Adds a flag column
    to indicate whether values are original or imputed.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame containing the column with NaN values.
    column_name : str
        The name of the column in which NaN values need to be filled.

    Returns:
    -------
    pd.DataFrame
        The DataFrame with NaN values replaced using linear interpolation,
        and an additional column marking imputed values.

    Raises:
    ------
    ValueError:
        If the column specified does not exist in the DataFrame, or if NaNs remain after interpolation.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")

    imputed_column_name = f"{column_name}_imputed"
    df[imputed_column_name] = df[column_name].isna()

    df[column_name] = df[column_name].interpolate(method='linear', limit_direction='both')

    df[column_name] = df[column_name].round().astype('Int64')

    try:
        validate_no_nans(df[[column_name]])
    except ValueError as e:
        logging.error(f"NaN validation failed after interpolation: {e}")
        raise

    # noinspection PyUnreachableCode
    logging.info(f"Successfully filled NaN values in '{column_name}' using interpolation. Added column '{imputed_column_name}' to track imputed values.")

    return df