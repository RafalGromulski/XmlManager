#!/usr/bin/env sh

python manage.py migrate --noinput
#python manage.py inspectdb --database=crldatabase > ./tsl_manager_app/models_crldatabase.py
python manage.py collectstatic --noinput
#service cron start
#python manage.py crontab add
python manage.py shell --no-startup --command="from django.contrib.auth.models import User; User.objects.create_superuser('xml', 'xml@xml.com',
'xml')"
#python ./tsl_validity_db_initialization.py
#python ./tsp_service_db_initialization.py
#gunicorn tsl_manager_project.wsgi --bind 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000