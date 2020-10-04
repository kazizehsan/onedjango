.PHONY:help

PROJECT_NAME_DEV = onedjango_dev
PROJECT_NAME_PROD = onedjango_prod
DOCKER_COMMAND_DEV = docker-compose -p $(PROJECT_NAME_DEV) -f docker/docker-compose.dev.yml
DOCKER_COMMAND_PROD = docker-compose -p $(PROJECT_NAME_PROD) -f docker/docker-compose.prod.yml

help: ## Help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

dev: ## Start development containers
	@echo "Starting development containers"
	@$(DOCKER_COMMAND_DEV) up -d --build db

down: ## Remove development containers
	@echo "Removing development containers"
	@$(DOCKER_COMMAND_DEV) down

clean: ## Remove development containers and volumes
	@echo "Removing development containers and volumes"
	@$(DOCKER_COMMAND_DEV) down -v

network: ## Create production docker network
	@echo "Creating production docker network"
	./docker/docker-network.sh

prod_up: network ## Start production containers
	@echo "Starting production containers"
	@$(DOCKER_COMMAND_PROD) up -d --build

prod_down: ## Remove production containers
	@echo "Removing production containers"
	@$(DOCKER_COMMAND_PROD) down

prod_clean: ## Remove production containers and volumes
	@echo "Removing production containers and volumes"
	@$(DOCKER_COMMAND_PROD) down -v