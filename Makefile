test:
	pip install -r requirements_dev.txt
	docker-compose -f docker-compose-test.yml up -d
	TEST=True py.test -s -v --cov=. --flakes
