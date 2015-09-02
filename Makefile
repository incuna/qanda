help:
	@echo "Usage:"
	@echo "    make help     -- display this help"
	@echo "    make test     -- run the tests"
	@echo "    make run      -- run the dev server"
	@echo "    make install  -- create the database, install requirements, etc"

test:
	python manage.py test

run:
	DEBUG=1 \
	EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend' \
	python manage.py runserver

install:
	pip install -r requirements.txt
ifeq ($(shell psql -tAc "SELECT 1 FROM pg_database WHERE datname='qanda';"), 1)
	@echo "Database already exists. Nothing to see here."
else
	@echo "Database does not exist, creating..."
	psql -c "CREATE DATABASE qanda;"
endif
	python manage.py migrate
