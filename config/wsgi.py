import os
import sys

from django.core.wsgi import get_wsgi_application

PROJECT_DIR_PATH = os.path.dirname(os.path.dirname(__file__))

if PROJECT_DIR_PATH not in sys.path:
    sys.path.append(PROJECT_DIR_PATH)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "config.settings.pro"
)

application = get_wsgi_application()
