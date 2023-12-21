py := poetry run
package_dir := src

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: api
api: ## Run API
	$(py) python -m $(package_dir).api.__main__

.PHONY: generate
generate: ## Generate alembic migration (name='Init')
	$(py) alembic revision --m="${name}" --autogenerate

.PHONY: migrate
migrate: ## Migrate to new revision
	$(py) alembic upgrade head

.PHONY: downgrade
downgrade: ## Downgrade to old revision
	$(py) alembic downgrade head