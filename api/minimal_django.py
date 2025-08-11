# Minimal Django handler for Vercel
import json
import os
import sys
import traceback

# Print debug information
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir()}")
print(f"Environment variables: {list(os.environ.keys())}")

# Set up Python path for Django
try:
    # Add the project root to the Python path
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    print(f"Updated sys.path: {sys.path}")
    
    # Set Django settings module to our minimal settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.minimal_settings')
    print(f"Django settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    
    # Import Django WSGI application
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    print("Django WSGI application successfully imported")
    
    # Create a handler that uses the Django WSGI application
    def handler(request, **kwargs):
        """A handler that uses a minimal Django WSGI application."""
        try:
            # Print request information
            print(f"Request path: {request.path}")
            print(f"Request method: {request.method}")
            
            # Call the Django WSGI application
            return application(request.environ, request.start_response)
        except Exception as e:
            error_message = f"Error in handler: {str(e)}"
            error_traceback = traceback.format_exc()
            print(error_message)
            print(error_traceback)
            
            # Return a JSON error response
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'status': 'error',
                    'message': error_message,
                    'traceback': error_traceback,
                    'python_version': sys.version,
                    'current_directory': os.getcwd(),
                    'environment_variables': list(os.environ.keys())
                }),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
except Exception as e:
    print(f"Error setting up Django: {e}")
    print(traceback.format_exc())
    
    # Fallback handler if Django cannot be loaded
    def handler(request, **kwargs):
        """Fallback handler when Django cannot be loaded."""
        error_message = f"Error loading Django: {str(e)}"
        error_traceback = traceback.format_exc()
        
        # Return a JSON error response
        return {
            'statusCode': 500,
            'body': json.dumps({
                'status': 'error',
                'message': error_message,
                'traceback': error_traceback,
                'python_version': sys.version,
                'current_directory': os.getcwd(),
                'sys_path': sys.path,
                'environment_variables': list(os.environ.keys())
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }