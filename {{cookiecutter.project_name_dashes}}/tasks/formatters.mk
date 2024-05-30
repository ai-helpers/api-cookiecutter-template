format-sources: ## Format the project sources.
	poetry run ruff format src/{{cookiecutter.project_name_underscores}}/ tests/

formatters: format-sources ## Run all the formatters.