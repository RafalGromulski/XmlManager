#!/usr/bin/env sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py shell --no-startup --command="from django.contrib.auth.models import User; User.objects.create_superuser('xml', 'xml@xml.com',
'xml')"
gunicorn xml_manager_project.wsgi --bind 0.0.0.0:8000
