#!/bin/bash -xe

export PYTHONPATH=/app:/app/Argus/src
DJANGO_SETTINGS_MODULE="kubernetes.settings"
export DJANGO_SETTINGS_MODULE
MANAGE_PATH=/app/Argus

cd $MANAGE_PATH
exec daphne -b 0.0.0.0 -p "$WS_PORT" argus.ws.asgi:application
