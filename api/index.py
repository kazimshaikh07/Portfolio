import os
import sys

# Point to the Django project dir containing manage.py
PROJECT_DIR = os.path.join(os.path.dirname(__file__), '..', 'portfolio')
PROJECT_DIR = os.path.abspath(PROJECT_DIR)

if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application  # noqa: E402
application = get_wsgi_application()

