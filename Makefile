test:
	@pip install -r requirements_dev.txt
	@docker-compose -f docker-compose-test.yml down  > /dev/null 2>&1 
	@docker-compose -f docker-compose-test.yml up -d
	@echo "Waiting database stay ready"
	@sleep 5
	@py.test src/ --create-db --flakes

dev:
	@pip install -r requirements_dev.txt
	@docker-compose -f docker-compose.yml up -d
	@python src/manage.py runserver 0.0.0.0:8000
	@echo "Running server in dev mode"

.PHONY: dev test