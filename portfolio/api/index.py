import os
import sys
from pathlib import Path

# Add the Django project to the Python path
current_dir = Path(__file__).resolve().parent
project_dir = current_dir.parent / 'portfolio'
sys.path.insert(0, str(project_dir))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
os.environ.setdefault('VERCEL', '1')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Export for Vercel
app = application
