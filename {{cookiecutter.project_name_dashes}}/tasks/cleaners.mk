clean-docs: ## Clean the documentations.
	rm -rf docs/build/
	rm -rf docs/source/_api/

clean-caches: ## Clean the project caches.
	rm -f .coverage*
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf .pytest_cache/

clean-python: ## Clean the Python caches.
	find . -type f -name '*.py[co]' -delete
	find . -type d -name __pycache__ -delete

clean-install: ## Clean the project install.
	rm -rf .venv/
	rm -f poetry.lock

clean-packages: ## Clean the project packages.
	rm -rf dist/

clean-reports: ## Clean the project generated reports.
	rm -rf reports/*.*

cleaners: clean-docs clean-caches clean-python clean-packages clean-reports ## Run all the cleaners.