import logging


def setup_logger() -> logging.Logger:
    """
    Sets up and returns a custom logger
    """
    logger = logging.getLogger("my-discord-bot")
    logger.setLevel(logging.INFO)

    # create console handler with a higher log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(console_handler)

    return logger
