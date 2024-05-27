import logging
import uvicorn

from {{cookiecutter.project_name_underscores}}.setup_logging import setup_logging
from {{cookiecutter.project_name_underscores}}.settings.app_settings import (Settings, get_settings)


def start_api() -> None:
    settings: Settings = get_settings()
    log_config: dict = setup_logging(log_level=settings.log_level)

    logger = logging.getLogger(__name__)
    logger.setLevel(settings.log_level)
    logger.info(f'[API] Log level set to {settings.log_level}')
    logger.info(f'[API] API service starting on {settings.svr_host}:{settings.svr_port}')

    uvicorn.run(
        "{{cookiecutter.project_name_underscores}}.app:app",
        host=settings.svr_host,
        port=settings.svr_port,
        root_path=settings.root_path,
        log_config=log_config,
        log_level=settings.log_level.lower(),
        workers=settings.workers
    )
    
if __name__ == "__main__":
    start_api()