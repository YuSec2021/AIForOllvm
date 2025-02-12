#!/bin/env python
import logging


from uvicorn.config import LOGGING_CONFIG
from settings import ENV_LOGGER_FORMATTER, ENV_ACCESS_LOGGER_FORMATTER

logger = logging.getLogger("uvicorn.error")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(
    logging.Formatter(
        fmt=ENV_LOGGER_FORMATTER.replace("%(levelprefix)s", "%(levelname)s:    ")
    )
)
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)

LOGGING_CONFIG["formatters"]["default"]["fmt"] = ENV_LOGGER_FORMATTER
LOGGING_CONFIG["formatters"]["access"]["fmt"] = ENV_ACCESS_LOGGER_FORMATTER
