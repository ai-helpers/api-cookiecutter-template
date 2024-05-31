import sys
import functools
import argparse
import pathlib
from typing import Optional, Union

import pydantic_settings

from {{cookiecutter.project_name_underscores}}.settings.args import parse_args
from {{cookiecutter.project_name_underscores}}.settings.defaults import (
    AI_MODEL_EXTERNAL_URL,
    DATA_LOADER_MODULE,
    LOCAL_DIR,
    LOCAL_TEMP_DIR,
    LOG_LEVEL,
    SVR_HOST,
    SVR_PORT,
    ROOT_PATH,
    WORKERS
)

class HashableBaseSettings(pydantic_settings.BaseSettings):
    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class Settings(HashableBaseSettings):
    ai_model_external_url: Union[str, pathlib.Path] = AI_MODEL_EXTERNAL_URL
    data_loader_module: Optional[str] = DATA_LOADER_MODULE
    local_dir: pathlib.Path = LOCAL_DIR
    local_temp_dir: pathlib.Path = LOCAL_TEMP_DIR
    log_level: str = LOG_LEVEL
    svr_host: str = SVR_HOST
    svr_port: int = SVR_PORT
    root_path: str = ROOT_PATH
    workers: int = WORKERS


@functools.lru_cache(maxsize=1, typed=False)
def get_settings() -> Settings:
    resulting_args: argparse.Namespace = parse_args(sys.argv[1:])

    # Map the log-level:
    # 0 -> WARNING (default); 1 -> INFO; 2 -> DEBUG)
    log_level_arg: str = LOG_LEVEL
    if resulting_args.log_level == 1:
        log_level_arg = "INFO"
    elif resulting_args.log_level == 2:
        log_level_arg = "DEBUG"

    settings: Settings = Settings(
        ai_model_external_url=resulting_args.ai_model_external_url,
        data_loader_module=resulting_args.data_loader_module,
        local_dir=resulting_args.local_dir,
        local_temp_dir=resulting_args.local_temp_dir,
        log_level=log_level_arg,
        svr_host=resulting_args.host,
        svr_port=resulting_args.port,
        root_path=resulting_args.root_path,
        workers=resulting_args.workers
    )
    return settings