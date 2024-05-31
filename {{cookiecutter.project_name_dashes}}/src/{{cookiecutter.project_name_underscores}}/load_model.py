import logging
import pydantic
import pickle
import pathlib
from cachetools.func import ttl_cache
from typing import Union


from {{cookiecutter.project_name_underscores}}.errors import (APIModelNotFoundError,
                                 APIModelNotLoadableError)
from {{cookiecutter.project_name_underscores}}.settings.app_settings import (Settings, get_settings)

@ttl_cache(maxsize=1, ttl=86400)
def load_model(settings: Settings):
    logger = logging.getLogger(__name__)
    logger.setLevel(settings.log_level)

    ai_model_external_url: Union[str, pathlib.Path] = settings.ai_model_external_url
   
    logger.info("[API::load_model] Machine Learning (ML) model " \
                f"pickle file: {ai_model_external_url}")

    # Read the Pickled model from the file-system
    model_filepath = pathlib.Path(ai_model_external_url)
    model = None
    if not model_filepath.exists():
        err_msg = f"[API::load_model] The model file " \
            "({model_filepath}) cannot be found"
        raise APIModelNotFoundError(err_msg)
     
    with open(model_filepath, 'rb') as f:
        logging.info("[API::load_model] Load model from " \
                     f"{model_filepath}...")
        model = pickle.load(f)

    if not model:
        err_msg = f"[API::load_model] The model file " \
            "({model_filepath}) cannot be loaded back into memory"
        raise APIModelNotLoadableError(err_msg)

    logging.info("[API::load_model] The ML model has been " \
                 f"successfully loaded from {model_filepath}")
    
    return model