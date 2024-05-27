import os
import pathlib

DATA_LOADER_MODULE = ""

MODEL_FILENAME = "model.pickle"
MODEL_LOCAL_REL_DIR = "data/models"

LOCAL_DIR = pathlib.Path(os.getcwd())
LOCAL_TEMP_DIR = pathlib.Path(os.getcwd()) / "tmp"
MODEL_LOCAL_DIR = LOCAL_DIR / MODEL_LOCAL_REL_DIR

MODEL_EXTERNAL_URL = MODEL_LOCAL_DIR / MODEL_FILENAME

LOG_LEVEL = "DEBUG"

SVR_HOST = "0.0.0.0"
SVR_PORT = 80

ROOT_PATH = "/"

WORKERS = 1