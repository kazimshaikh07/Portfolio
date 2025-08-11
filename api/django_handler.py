# Simple Django-compatible handler for Vercel
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
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(f"Updated sys.path: {sys.path}")
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
    print(f"Django settings module: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
    
    # Import Django settings to check if it works
    from django.conf import settings
    print(f"Django settings imported successfully. DEBUG={settings.DEBUG}")
    
    # Create a simple handler that returns Django settings info
    def handler(request, **kwargs):
        """A simple Django-compatible handler for Vercel."""
        try:
            # Print request information
            print(f"Request path: {request.path}")
            print(f"Request method: {request.method}")
            
            # Collect Django settings information
            info = {
                'status': 'ok',
                'message': 'Django settings loaded successfully',
                'django_debug': settings.DEBUG,
                'django_allowed_hosts': settings.ALLOWED_HOSTS,
                'django_installed_apps': settings.INSTALLED_APPS,
                'django_middleware': settings.MIDDLEWARE,
                'django_database_engine': settings.DATABASES['default']['ENGINE'],
                'python_version': sys.version,
                'current_directory': os.getcwd(),
                'environment_variables': list(os.environ.keys())
            }
            
            # Return a JSON response
            return {
                'statusCode': 200,
                'body': json.dumps(info),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
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
    
    # Fallback handler if Django settings cannot be loaded
    def handler(request, **kwargs):
        """Fallback handler when Django settings cannot be loaded."""
        error_message = f"Error loading Django settings: {str(e)}"
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