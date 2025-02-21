import logging

import pandas as pd


def write_csv_data(df: pd.DataFrame, file_path: str, encoding: str = "utf-8") -> None:
    """
    Saves a DataFrame to a CSV file with error handling and logging.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame to be saved.
    file_path : str
        The path where the CSV file will be saved.
    encoding : str, optional
        The file encoding (default: 'utf-8').

    Raises:
    ------
    ValueError:
        If the DataFrame is empty.
    IOError:
        If there is an issue writing the file.
    """
    try:
        if df.empty:
            raise ValueError("Cannot save an empty DataFrame.")

        df.to_csv(file_path, index=False, encoding=encoding)

        logging.info(f"CSV file '{file_path}' saved successfully with {df.shape[0]} rows and {df.shape[1]} columns.")

    except ValueError as e:
        logging.error(f"DataFrame is empty: {e}")
        raise
    except IOError as e:
        logging.error(f"Error writing CSV file '{file_path}': {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error while saving CSV file '{file_path}': {e}")
        raise
