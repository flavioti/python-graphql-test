run:
	#python ./manage.py runserver
	export FLASK_ENV=development
	flask run


test:
	make codequality
	python3 -m pytest -v --cov=src

codequality:
	black src

virtualenv:
	virtualenv --python='/usr/bin/python3' env
	make installpkgdev

installpkgdev:
	pip install -r requirements-dev.txt

clean:
	make clean-python clean-test

clean-python:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache/
