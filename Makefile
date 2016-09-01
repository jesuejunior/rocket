test:
	@pip install -r requirements_dev.txt
	@docker-compose -f docker-compose-test.yml down 
	@docker-compose -f docker-compose-test.yml up -d
	@echo "Waiting database stay ready"
	@sleep 5
	@py.test --create-db --flakes
