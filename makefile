HOST=$(shell hostname)

all: install migrate lint server

server:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py runserver 8000

debug:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 -m debugpy --listen 0.0.0.0:6969 --wait-for-client  manage.py runserver 8080

clean:
	rm -rf env/

install:
	python3.9 -m venv env
	. env/bin/activate && pip3.9 --version
	. env/bin/activate && python3.9  -m pip install --upgrade pip
	. env/bin/activate && pip3.9 --version
	. env/bin/activate && pip3.9 install -r requirements.txt

migrate:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py migrate 

revert_migrate:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py migrate ${app} ${migration}

migrations:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py makemigrations

empty-migrations:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py makemigrations --empty ${app} 

superuser:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py createsuperuser

startapp:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py startapp ${app_name}

format:
	. env/bin/activate && black .

lint:
	. env/bin/activate && pylint --fail-under 9.0 --load-plugins pylint_django --disable=duplicate-code core/*.py accounts/*.py

test:
	TESTS_DB="True" DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py test --pattern="test_*.py"

test_app:
	TESTS_DB="True" DJANGO_SETTINGS_MODULE=app.settings.${setting} . env/bin/activate && python3.9 manage.py test ${app} --pattern="test_*.py"

shell:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py shell

makemessages:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py makemessages -l en --ignore env*
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py makemessages -l ar --ignore env*

compilemessages:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py compilemessages

collect_static:
	DJANGO_SETTINGS_MODULE=core.settings . env/bin/activate && python3.9 manage.py collectstatic

greenkeeping:
	. env/bin/activate && pur -r requirements.txt
