isset-%: ## Test if variable % is set or exit with error.
	# @: $(if $(value $*),,$(error Variable $* is not set))