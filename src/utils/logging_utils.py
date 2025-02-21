import logging


def setup_logging(level: int = logging.DEBUG) -> None:
    """
    Configures the logging for the application with the specified log level.
    Also suppresses excessive debug logs from Matplotlib.

    Parameters:
    ----------
    level : int, optional
        The logging level to set (e.g., logging.DEBUG, logging.INFO). Defaults to logging.DEBUG.

    Raises:
    ------
    Exception:
        Reraises any exception that occurs during the logging setup.

    Example:
    -------
    >>> setup_logging()
    """
    try:
        logging.root.handlers.clear()

        logging.basicConfig(
            level=level,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )

        logging.getLogger("matplotlib").setLevel(logging.WARNING)

        logging.info("Logging has been configured successfully.")
    except Exception as e:
        logging.error("Failed to configure logging.", exc_info=True)
        raise e