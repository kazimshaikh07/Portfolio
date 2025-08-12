import os
import sys
from pathlib import Path

# Ensure project package is importable
CURRENT_FILE = Path(__file__).resolve()
PROJECT_DIR = CURRENT_FILE.parent  # .../portfolio/portfolio
DJANGO_PROJECT_ROOT = PROJECT_DIR.parent  # .../portfolio

# Add the Django project root to Python path
if str(DJANGO_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(DJANGO_PROJECT_ROOT))

# Set environment variables for Vercel
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
os.environ.setdefault('VERCEL', '1')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()


