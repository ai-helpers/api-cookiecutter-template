import pathlib
import fastapi

from {{cookiecutter.project_name_underscores}}.endpoints.router import router

endpoint_description = """
Dump the content of the data/info.txt file when it exists.
The source for that info.txt file is
"""

@router.get('/info', description=endpoint_description,
            status_code=fastapi.status.HTTP_200_OK)
async def info():
   file_content = None
   file_path = pathlib.Path('data/info.txt')
   if file_path.exists():
      with open(file_path) as f:
         file_content = f.read()
           
   return file_content