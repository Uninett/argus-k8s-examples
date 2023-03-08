#!/bin/bash -xe

export PYTHONPATH=/app:/app/Argus/src
DJANGO_SETTINGS_MODULE="kubernetes.settings"
export DJANGO_SETTINGS_MODULE
MANAGE_PATH=/app/Argus

cd $MANAGE_PATH
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
exec gunicorn --forwarded-allow-ips="*" --log-level debug --access-logfile - kubernetes.wsgi -b 0.0.0.0:$PORT
