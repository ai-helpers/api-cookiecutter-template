import fastapi

from {{cookiecutter.project_name_underscores}}.endpoints.router import router

endpoint_description = """
Returns "OK" with a 200 status code (meaning that everything is fine).

That API endpoint may be used for instance for livelyness and readyness probes.
"""

@router.get('/healthcheck', description=endpoint_description,
            status_code=fastapi.status.HTTP_200_OK)
async def healthcheck() -> str:
   return "OK"