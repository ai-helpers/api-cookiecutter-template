# https://www.gnu.org/software/make/manual/make.html

## HELP

.DEFAULT_GOAL:=help
help: ## List all make tasks
	@grep --no-filename "##" tasks/*.mk | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

## TASKS

include tasks/helpers.mk
include tasks/builders.mk
include tasks/bumpers.mk
include tasks/checkers.mk
include tasks/cleaners.mk
include tasks/documenters.mk
include tasks/formatters.mk
