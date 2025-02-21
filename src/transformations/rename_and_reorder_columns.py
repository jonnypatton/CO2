import pandas as pd

def rename_and_reorder_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renames the 'state' column to 'co2_ppm' and reorders the columns.

    The new column order:
    - entity_id
    - co2_ppm
    - state_imputed (unchanged)
    - 15_point_ema
    - last_changed

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame containing the CO₂ sensor data.

    Returns:
    -------
    pd.DataFrame
        The DataFrame with renamed and reordered columns.

    Raises:
    ------
    ValueError:
        If the 'state' column is missing.
    """
    # Ensure 'state' exists before renaming
    if "state" not in df.columns:
        raise ValueError("Column 'state' not found in DataFrame.")

    # Rename 'state' -> 'co2_ppm'
    df = df.rename(columns={"state": "co2_ppm"})

    # Define expected column order
    column_order = ["entity_id", "co2_ppm", "state_imputed", "15_point_ema", "last_changed"]

    # Reorder columns while keeping any extra columns
    df = df[[col for col in column_order if col in df.columns] +
            [col for col in df.columns if col not in column_order]]

    return df