build-%: ## Build package for format %.
	poetry build --format=$*

builders: build-wheel ## Run all the builders.