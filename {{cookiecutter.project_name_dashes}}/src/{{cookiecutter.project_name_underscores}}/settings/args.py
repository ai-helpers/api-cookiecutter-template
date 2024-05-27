import argparse
import pydantic
import typing

from {{cookiecutter.project_name_underscores}}.settings.defaults import (
    MODEL_EXTERNAL_URL,
    DATA_LOADER_MODULE,
    LOCAL_DIR,
    LOCAL_TEMP_DIR,
    LOG_LEVEL,
    SVR_HOST,
    SVR_PORT,
    ROOT_PATH,
    WORKERS
)
from {{cookiecutter.project_name_underscores}} import __version__

def _add_version(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-V", "--version",
      action="version",
      version=f"{__version__} (API)",
   )
   return parser

def _add_log_level(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-v", "--log-level",
      help="logging level. Default is silent (0/WARNING). `-v` corresponds to 1/INFO. `-vv` corresponds to 2/DEBUG.",
      action="count",
      dest="log_level",
      default=2,
   )
   return parser

def _add_host(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-H", "--host",
      help=f"IP address of the host on which the API service is started (e.g., {SVR_HOST}).",
      action="store",
      default=SVR_HOST,
   )
   
   return parser

def _add_port(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-p", "--port",
      help=f"port on which the API service is listening the incoming requests (e.g., {SVR_PORT}).",
      type=int,
      action="store",
      default=SVR_PORT,
   )
   return parser

def _add_workers(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-w", "--workers",
      help=f"number of worker processes in the Uvicorn server (e.g., {WORKERS}).",
      type=int,
      action="store",
      default=WORKERS
   )
   return parser


def _add_root_path(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument(
        "-r", "--root-path",
        help=f"prefix in the URL/path of the REST API (e.g., '{ROOT_PATH}').",
        dest="root_path",
        action="store",
        default=ROOT_PATH
    )
    return parser


def _add_data_loader_module(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-d", "--data-loader-module",
      help=f"data loader module (e.g., '{DATA_LOADER_MODULE}').",
      dest="data_loader_module",
      action="store",
      default=DATA_LOADER_MODULE
   )
   return parser

def _add_local_dir(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-l", "--local-dir",
      help=f"local permanent directory for file storage (e.g., '{LOCAL_DIR}').",
      dest="local_dir",
      action="store",
      default=LOCAL_DIR
   )
   return parser


def _add_local_temp_dir(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-t", "--local-temp-dir",
      help=f"local temporary directory for file storage (e.g., '{LOCAL_TEMP_DIR}')",
      dest="local_temp_dir",
      action="store",
      default=LOCAL_TEMP_DIR
   )
   return parser

def _add_model_external_url(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
   parser.add_argument(
      "-m", "--model-external-url",
      help=f"URL (if remote) or file-path (if local) of the Pickled/serialized ML model (e.g., '{MODEL_EXTERNAL_URL}').",
      dest="model_external_url",
      action="store",
      default=MODEL_EXTERNAL_URL
   )
   return parser

def _get_arg_parser() -> argparse.ArgumentParser:
   parser = argparse.ArgumentParser(
      description=(
         "API command-line (CLI) tool. "
         "That utility launches a Uvicorn/FastAPI server, "
      )
   )

   parser = _add_version(parser)
   parser = _add_log_level(parser)
   parser = _add_host(parser)
   parser = _add_port(parser)
   parser = _add_workers(parser)
   parser = _add_root_path(parser)
   parser = _add_data_loader_module(parser)
   parser = _add_local_dir(parser)
   parser = _add_local_temp_dir(parser)
   parser = _add_model_external_url(parser)
   
   return parser

def parse_args(args: typing.List[str] = None) -> argparse.Namespace:
   parser: argparse.ArgumentParser = _get_arg_parser()
   resulting_args: argparse.Namespace = parser.parse_args(args)
   return resulting_args