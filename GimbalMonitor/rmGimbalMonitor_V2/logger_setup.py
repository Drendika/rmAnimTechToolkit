"""
setup_logger.py
Logging system for the entire tool.
"""

import logging
from pathlib import Path
import sys

_LOG_DIR: Path = Path(__file__).resolve().parent / "Logs"
_LOG_PATH: Path = _LOG_DIR / "GimbalMonitor_LOG.log"

def setupLogger(name: str) -> logging.Logger:
    """
    Execute for all files from rmGimbalMonitor_V2 root folder.
    In each .py file has been set "logger = logging.getLogger(__name__)".
    Each .py file has its own logger.
    """
    if not _LOG_DIR.is_dir(): # Checking the log folder. If it doesn't exist, create the folder "Log".
        _LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False # Disables sending logs to the root logger (Maya's logger)

    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    fileHandler = logging.FileHandler(_LOG_PATH, mode="w")
    fileHandler.setLevel(logging.DEBUG) # TODO Зміни перед релізом
    fileHandlerFormatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s: %(filename)s|L%(lineno)d — %(message)s", datefmt="%H:%M:%S"
    )
    fileHandler.setFormatter(fileHandlerFormatter)
    logger.addHandler(fileHandler)

    streamHandler = logging.StreamHandler(sys.stderr)
    streamHandler.setLevel(logging.DEBUG) # TODO Зміни перед релізом
    streamHandlerFormatter = logging.Formatter("%(levelname)s: %(message)s")
    streamHandler.setFormatter(streamHandlerFormatter)
    logger.addHandler(streamHandler)

    return logger

# TODO Виріши що все ж таки використовувати, dictConfig чи вже як є?
""" 
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "fileHandlerFormatter": {
            "format": "%(levelname)s: [%(filename)s:%(lineno)d]: %(message)s",
        },
        "streamHandlerFormatter": {
            "format": "%(levelname)s: [%(filename)s:%(lineno)d]: %(message)s",
        }

    },
    "handlers": {
        "fileHandlerFormatter": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "fileHandlerFormatter",
            "stream": "ext://sys.stderr",
            "maxBytes": 10000000, # 10 MB
            "backupCount": 5,
            "level": "DEBUG",
        },
        "streamHandler": {
            "class": "logging.StreamHandler",
            "formatter": "streamHandlerFormatter",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
        }
    },
    "loggers": {
        "root": {"level": "DEBUG", "handlers": ["fileHandlerFormatter", "streamHandler"]},
    }
}
"""