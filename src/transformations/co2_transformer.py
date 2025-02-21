import logging

import pandas as pd

from src.transformations.add_ema_column import add_ema_column
from src.transformations.convert_to_datetime import convert_to_datetime
from src.transformations.convert_to_numeric import convert_to_numeric
from src.transformations.fill_nans_with_mean import fill_nans_with_mean
from src.transformations.rename_and_reorder_columns import rename_and_reorder_columns


def transform_co2_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies all transformations to the CO₂ dataset in sequence.

    The transformations applied:
    1. Converts 'state' to numeric.
    2. Converts 'last_changed' to datetime.
    3. Fills NaNs in 'state' using interpolation and adds an imputation flag.
    4. Adds a 15-point EMA column.
    5. Renames 'state' to 'co2_ppm' and reorders the columns.

    Parameters:
    ----------
    df : pd.DataFrame
        The raw CO₂ data DataFrame.

    Returns:
    -------
    pd.DataFrame
        The fully transformed CO₂ DataFrame.

    Raises:
    ------
    ValueError:
        If any step fails due to missing or invalid data.
    """
    try:
        logging.info("Starting CO₂ data transformation pipeline.")

        df = convert_to_numeric(df, 'state')
        df = convert_to_datetime(df, 'last_changed')
        df = fill_nans_with_mean(df, 'state')
        df = add_ema_column(df)  # Uses default 'state'
        df = rename_and_reorder_columns(df)

        logging.info("CO₂ data transformation pipeline completed successfully.")
        return df

    except Exception as e:
        logging.error(f"Error in CO₂ transformation pipeline: {e}", exc_info=True)
        raise
