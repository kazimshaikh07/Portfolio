import os
import sys
import traceback
from pathlib import Path
import json

# Enhanced error handling and debugging
def debug_info():
    info = {
        "python_version": sys.version,
        "sys_path": sys.path,
        "current_directory": os.getcwd(),
        "directory_contents": os.listdir('.'),
        "environment_variables": list(os.environ.keys())
    }
    print(f"Debug info: {json.dumps(info, indent=2)}")

try:
    # Load environment variables from .env file if available
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("Environment variables loaded from .env file")
    except ImportError:
        print("dotenv module not available, skipping .env loading")
    except Exception as e:
        print(f"Error loading .env file: {e}")
    
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
    
    # Check if DJANGO_ROOT exists and list its contents
    if os.path.exists(DJANGO_ROOT):
        print(f"Files in DJANGO_ROOT: {os.listdir(DJANGO_ROOT)}")
    else:
        print(f"DJANGO_ROOT directory not found: {DJANGO_ROOT}")
        # Try to find the Django project directory
        possible_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(os.path.join(d, 'manage.py'))]
        print(f"Possible Django project directories: {possible_dirs}")
    
    # Call debug_info function to print detailed debug information
    debug_info()
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    print(f"Django settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    
    # Import Django WSGI application with detailed error handling
    try:
        print("Attempting to import Django WSGI application...")
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        print("Django WSGI application successfully imported")
    except ImportError as e:
        print(f"ImportError when importing Django WSGI application: {e}")
        print(traceback.format_exc())
        raise
    except Exception as e:
        print(f"Unexpected error when importing Django WSGI application: {e}")
        print(traceback.format_exc())
        raise
    
    # For Vercel serverless functions
    app = application
    print("WSGI application setup complete")
    
except Exception as e:
    print(f"Error in wsgi.py: {e}")
    print(traceback.format_exc())
    
    # Create a simple WSGI application that returns an error message
    def application(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'application/json')]
        start_response(status, response_headers)
        error_info = {
            'status': 'error',
            'message': f'Django application failed to load: {str(e)}',
            'traceback': traceback.format_exc()
        }
        return [json.dumps(error_info).encode()]
    
    # For Vercel serverless functions
    app = application
    raise