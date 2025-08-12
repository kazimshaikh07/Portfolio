import os
import sys
from pathlib import Path

# Add the project to Python path
current_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(current_dir))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
os.environ.setdefault('VERCEL', '1')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
