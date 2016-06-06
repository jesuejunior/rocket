test:
	pip install -r requirements_dev.txt
	docker-compose up -d
	TEST=True py.test -s -v --cov=.