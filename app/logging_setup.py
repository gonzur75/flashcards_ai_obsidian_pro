import atexit
import logging.config
import os
import tomllib
from logging import Handler
from pathlib import Path
from typing import Any


def setup_logging() -> None:
    if os.getenv("TESTS") == "1":
        return None

    config_file: Path = Path(".logging_configs/config.toml")
    with open(config_file, "rb") as file:
        config: dict[str, Any] = tomllib.load(file)

    logging.config.dictConfig(config)

    queue_handler: Handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)  # type: ignore [attr-defined]
