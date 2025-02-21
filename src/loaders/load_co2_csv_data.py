import logging
from typing import Optional

import pandas as pd


def load_co2_csv_data(file_path: str, delimiter: str = ",", encoding: str = "utf-8",
                      ) -> Optional[pd.DataFrame]:
    """
    Loads a CO₂ CSV dataset into a Pandas DataFrame with error handling and logging.
    This function is designed to be future-proof for CO₂-specific data processing.

    Parameters:
    ----------
    file_path : str
        The path to the CO₂ CSV file.
    delimiter : str, optional
        The delimiter used in the file (default: ',').
    encoding : str, optional
        The file encoding (default: 'utf-8').

    Returns:
    -------
    Optional[pd.DataFrame]
        The loaded DataFrame if successful, otherwise None.

    Raises:
    ------
    FileNotFoundError:
        If the file does not exist.
    ValueError:
        If there is an issue parsing the CSV file.

    Future Enhancements:
    --------------------
    - Custom CO₂ data cleaning (column renaming, type conversion, outlier handling)
    - Automatic unit conversions (ppm, mg/m³)
    - Date-time standardization for different CO₂ sources
    """
    try:
        df = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)

        logging.info(
            f"CO₂ CSV file '{file_path}' loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        logging.error(f"File is empty: {file_path}")
    except pd.errors.ParserError:
        logging.error(f"Error parsing file: {file_path}")
    except Exception as e:
        logging.error(f"Unexpected error loading CO₂ CSV file '{file_path}': {e}")

    return None
