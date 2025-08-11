import os
import sys
from pathlib import Path

# Build paths properly for Vercel deployment
BASE = Path(__file__).resolve().parent.parent
DJANGO_ROOT = BASE / 'portfolio'

# Add both the Django project root and the repository root to the path
for p in (str(DJANGO_ROOT), str(BASE)):
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Vercel requires a handler function
def handler(request, **kwargs):
    return application(request.environ, request.start_response)

