test:
	@pip install -r requirements_dev.txt
	@docker-compose -f docker-compose-test.yml down  > /dev/null 2>&1 
	@docker-compose -f docker-compose-test.yml up -d
	@echo "Waiting database stay ready"
	@sleep 5
	@py.test --create-db --flakes
	@echo "Tests finished"
