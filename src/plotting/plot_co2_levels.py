import logging

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.dates import DateFormatter


def plot_co2_levels(df: pd.DataFrame, time_column: str = 'last_changed',
                    co2_column: str = 'state', ema_column: str = '15_point_ema') -> None:
    """
    Plots CO₂ levels with a 15-point EMA and hourly vertical lines.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame containing CO₂ data.
    time_column : str, optional
        The name of the datetime column (default: 'last_changed').
    co2_column : str, optional
        The name of the CO₂ level column (default: 'state').
    ema_column : str, optional
        The name of the EMA column (default: '15_point_ema').

    Raises:
    ------
    ValueError:
        If any required columns are missing in the DataFrame.

    Example:
    -------
    >>> plot_co2_levels(df)
    """
    # Validate required columns
    for col in [time_column, co2_column, ema_column]:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in DataFrame.")

    try:
        plt.rcParams["font.family"] = "DejaVu Sans"

        plt.figure(figsize=(12, 6))

        # Light blue for CO2 levels
        sns.lineplot(data=df, x=time_column, y=co2_column, label='CO₂ Levels', color='lightblue')

        # Dark blue for EMA
        sns.lineplot(data=df, x=time_column, y=ema_column, label='15-Point EMA', color='darkblue')

        # Add hourly vertical lines
        for hour in pd.date_range(start=df[time_column].min().floor('h'),
                                  end=df[time_column].max().ceil('h'), freq='h'):
            plt.axvline(x=hour, color='gray', linestyle='--', alpha=0.5)

        # Format x-axis
        plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))

        plt.title('CO₂ Levels with Hourly Markers')
        plt.xlabel('Time (HH:MM)')
        plt.ylabel('CO₂ Level (ppm)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()

        plt.show()
        logging.info("Successfully plotted CO₂ levels.")

    except Exception as e:
        logging.error(f"Error while plotting CO₂ levels: {e}", exc_info=True)
        raise
