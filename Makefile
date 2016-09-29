test:
	@pip install -r requirements_dev.txt
	#@docker-compose -f docker-compose-test.yml rm --rmi local  > /dev/null 2>&1
	@docker-compose -f docker-compose-test.yml up -d
	@echo "Waiting database stay ready"
	@sleep 5
	@py.test src/ --create-db --flakes

dev:
	@pip install --upgrade pip
	@pip install -r requirements_dev.txt
	@docker-compose -f docker-compose.yml up -d
	@sleep 3
	@python src/manage.py migrate
	@python src/manage.py runserver 0.0.0.0:8000
	@echo "Running server in dev mode"

checker:
	@pep8 --show-source --show-pep8

.PHONY: test dev
