import os
import sys

from django.core.wsgi import get_wsgi_application

DEPLOY_HOME = os.path.abspath('__file__')
APP_HOME = os.path.dirname(DEPLOY_HOME)
sys.path.append(os.path.join(APP_HOME, 'Argus/src'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kubernetes.settings")

application = get_wsgi_application()
