import os
import sys
import traceback
from pathlib import Path

try:
    # Load environment variables from .env file if available
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    
    # Build paths properly for Vercel deployment
    BASE = Path(__file__).resolve().parent.parent
    DJANGO_ROOT = BASE / 'portfolio'
    
    # Add paths to sys.path
    paths_to_add = [str(DJANGO_ROOT), str(BASE), str(DJANGO_ROOT.parent)]
    for p in paths_to_add:
        if p not in sys.path:
            sys.path.insert(0, p)
    
    # Debug information
    print(f"Python path: {sys.path}")
    print(f"Current directory: {os.getcwd()}")
    print(f"BASE: {BASE}")
    print(f"DJANGO_ROOT: {DJANGO_ROOT}")
    print(f"Files in DJANGO_ROOT: {os.listdir(DJANGO_ROOT) if os.path.exists(DJANGO_ROOT) else 'Directory not found'}")
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    
    # Import Django WSGI application
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    
    # For Vercel serverless functions
    app = application
    
except Exception as e:
    print(f"Error in wsgi.py: {e}")
    print(traceback.format_exc())
    raise