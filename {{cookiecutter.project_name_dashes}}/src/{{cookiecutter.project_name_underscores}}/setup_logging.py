import logging

from {{cookiecutter.project_name_underscores}} import __version__
from {{cookiecutter.project_name_underscores}}.settings.defaults import LOG_LEVEL


def setup_logging(log_level: str = LOG_LEVEL) -> dict:
    log_format = "[\%(asctime)s] {\%(name)s} \%(levelname)s - \%(message)s"

    logging.basicConfig(level=log_level, format=log_format)

    logging.info(f"[API] Starting service with version {__version__}...")
    logging.info(f"[API] Log level set to {log_level}")

    log_config: dict = {
        "version": 1,
        "formatters": {"default": {"format": log_format}},
        "handlers": {
            "console": {
                "formatter": "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "level": log_level,
            }
        },
        "root": {"handlers": ["console"], "level": log_level},
        "loggers": {
            "gunicorn": {"propagate": True},
            "uvicorn": {"propagate": True},
            "uvicorn.access": {"propagate": True},
        },
    }
    
    return log_config