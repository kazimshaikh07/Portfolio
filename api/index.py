import os
import sys
import traceback
from pathlib import Path

try:
    # Load environment variables from .env file if available
    from dotenv import load_dotenv
    load_dotenv()
    
    # Build paths properly for Vercel deployment
    BASE = Path(__file__).resolve().parent.parent
    DJANGO_ROOT = BASE / 'portfolio'
    
    # Add both the Django project root and the repository root to the path
    for p in (str(DJANGO_ROOT), str(BASE)):
        if p not in sys.path:
            sys.path.insert(0, p)
    
    # Print paths for debugging
    print(f"Python path: {sys.path}")
    print(f"Current directory: {os.getcwd()}")
    print(f"BASE: {BASE}")
    print(f"DJANGO_ROOT: {DJANGO_ROOT}")
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    
    # Import Django WSGI application
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    
    # Vercel serverless function handler
    def handler(request, **kwargs):
        """Handle a request to the Vercel serverless function."""
        try:
            return application(request.environ, request.start_response)
        except Exception as e:
            print(f"Error in handler: {e}")
            print(traceback.format_exc())
            raise
    
    # For Vercel serverless functions
    app = application
    
except Exception as e:
    print(f"Error during initialization: {e}")
    print(traceback.format_exc())
    raise

