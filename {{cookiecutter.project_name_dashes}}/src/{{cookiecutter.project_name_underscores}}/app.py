import fastapi

from {{cookiecutter.project_name_underscores}} import __version__
from {{cookiecutter.project_name_underscores}}.endpoints import (root, health, info, test, predict)

#
app = fastapi.FastAPI(
   title="API",
   description="{{cookiecutter.description}}",
   version=__version__,
)

# Register the endpoints. See the endpoints/ directory
# for the corresponding source code.
app.include_router(root.router)
app.include_router(health.router)
app.include_router(info.router)
app.include_router(test.router)
app.include_router(predict.router)