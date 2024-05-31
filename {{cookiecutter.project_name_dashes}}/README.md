**API - {{cookiecutter.project_long_name}}**

- **Template**: [AI Helpers API template](https://github.com/ai-helpers/api-cookiecutter-template)
- **Description**: {{cookiecutter.description}}

## Table of Content (ToC)

- [Table of Content (ToC)](#table-of-content-toc)
- [Quickstart](#quickstart)
- [Endpoints](#endpoints)
  - [Health](#health)
  - [Info](#info)
  - [Predict](#predict)
  - [Test](#test)
  - [Documentation](#documentation)
- [Project Structure](#project-structure)
- [Contributions](#contributions)

## Quickstart

```bash
$ poetry install
[...]
Package operations: 44 installs, 0 updates, 0 removals
[...]
$ poetry run api-example
[\2024-05-28 15:58:59,332] {\root} \INFO - \[API] Starting service with version 0.1.0...
[\2024-05-28 15:58:59,332] {\root} \INFO - \[API] Log level set to DEBUG
[\2024-05-28 15:58:59,332] {\api_example.cli} \INFO - \[API] Log level set to DEBUG
[\2024-05-28 15:58:59,332] {\api_example.cli} \INFO - \[API] API service starting on 0.0.0.0:80
[\2024-05-28 15:59:15,529] {\uvicorn.error} \INFO - \Started server process [98569]
[\2024-05-28 15:59:15,529] {\uvicorn.error} \INFO - \Waiting for application startup.
[\2024-05-28 15:59:15,529] {\uvicorn.error} \INFO - \Application startup complete.
[\2024-05-28 15:59:15,534] {\uvicorn.error} \INFO - \Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

## Endpoints

### Health
A simple endpoint to check the health of the application.
```http
GET /health
```
Returns a status message indicating the service is up and running.

### Info
Provides information about the application.
```http
GET /info
```
Returns metadata such as version, author, and other relevant details (cf. `data/info.txt`)

### Predict
Endpoint for making predictions based on input data.
```http
POST /predict
```
Accepts a JSON payload with the necessary input data and returns the prediction results.

### Test
Endpoint for testing purposes.
```http
GET /test
```
Returns a test response, useful for debugging and ensuring the endpoint is reachable.

### Documentation
FastAPI provides interactive API documentation.
```http
GET /docs
```
Access the Swagger UI for a user-friendly interface to interact with your API.

```http
GET /redoc
```
Access the ReDoc interface for an alternative documentation style.

## Project Structure

    ├── {{cookiecutter.project_name_dashes}}
    │   ├── .github                                         <- Github Actions CICD
    │   ├── data
    │   ├── docs                                            <- Sphinx documentation
    │   ├── src   
    │       └── {{cookiecutter.project_name_underscores}}   <- Core of project
    │   │       ├── endpoints                               <- API endpoints definition
    │   │       ├── settings                                <- settings
    │   │       ├── __init__.py      
    │   │       ├── app.py           
    │   │       ├── cli.py           
    │   │       ├── errors           
    │   │       ├── load_model.py    
    │   │       └── setup_logging.py 
    │   ├── tasks                                           <- Makefile tasks
    │   ├── tests                                           <- tests (units tests, data tests)
    │   ├── .gitignore          
    │   ├── .mypy.ini   
    │   ├── Makefile   
    │   ├── poetry.toml                       
    │   ├── pyproject.toml   
        └── README.md    

## Contributions

Your contributions are valued! Please feel free to open issues or submit pull requests.

Let me know if you'd like any other sections added!