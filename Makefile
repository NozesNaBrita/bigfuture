clean:
	find . -name \*.pyc -delete
	find . -name \*__pycache__ -delete

lint:
	flake8 .

test: clean lint
	DJANGO_SETTINGS_MODULE=bigfuture.settings.test python manage.py test

urls:
	python manage.py show_urls

db:
	rm -rf bigfuture/db.sqlite3
	python manage.py makemigrations
	python manage.py migrate

install:
	pip install -U -r requirements.txt

install-test:
	pip install -U -r requirements.test.txt

start: clean
	DJANGO_SETTINGS_MODULE=bigfuture.settings.base ./manage.py runserver 9000
