import os
import sys
from pathlib import Path

# Ensure project package is importable
CURRENT_FILE = Path(__file__).resolve()
PROJECT_DIR = CURRENT_FILE.parent  # .../portfolio/portfolio
REPO_ROOT = PROJECT_DIR.parent.parent  # repo root
DJANGO_PROJECT_ROOT = PROJECT_DIR.parent  # .../portfolio

for p in (str(DJANGO_PROJECT_ROOT), str(REPO_ROOT)):
    if p not in sys.path:
        sys.path.insert(0, p)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()


