test:
	pip install -r requirements_dev.txt
	docker-compose -f docker-compose-test.yml up -d
	py.test --reuse-db --flakes
