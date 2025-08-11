import os
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DJANGO_ROOT = BASE / 'portfolio'
if str(DJANGO_ROOT) not in sys.path:
    sys.path.insert(0, str(DJANGO_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

