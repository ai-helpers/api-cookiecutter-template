import fastapi

from {{cookiecutter.project_name_underscores}}.endpoints.router import router

DEFAULT_OUTPUT = {
    # "feature_1": {"type": "float64", "example": -0.02596975},
}

def format_output_json(dict_):
   """
   Transform the dict with example keys and into format as json.

    :param dict_:
    :return:
   """
   result = {key: value["example"] for key, value in dict_.items()}
   return result

endpoint_description = """
Returns a default dictionary of values, normally with the same format as
ordinary predictions.
"""

@router.get('/test', description=endpoint_description,
            status_code=fastapi.status.HTTP_200_OK)
async def test() -> dict:
   output_data = format_output_json(DEFAULT_OUTPUT)
   return output_data