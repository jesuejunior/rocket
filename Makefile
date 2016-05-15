test:
	pip install -r requirements_dev.txt && pip install -r requirements.txt

	TEST=True py.test -s -v --cov=.