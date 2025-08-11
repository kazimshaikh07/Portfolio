# Simple WSGI application for testing Vercel deployment
import os
import sys
import json
import traceback

# Print debug information
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir()}")
print(f"Environment variables: {list(os.environ.keys())}")

# Simple WSGI application
def application(environ, start_response):
    """A simple WSGI application that returns a JSON response."""
    status = '200 OK'
    response_headers = [('Content-type', 'application/json')]
    start_response(status, response_headers)
    
    # Collect environment information
    info = {
        'status': 'ok',
        'message': 'Simple WSGI application is working',
        'python_version': sys.version,
        'current_directory': os.getcwd(),
        'environment_variables': list(os.environ.keys()),
        'wsgi_environ': {
            key: str(value) for key, value in environ.items()
            if isinstance(value, (str, int, float, bool, type(None)))
        }
    }
    
    # Return a JSON response
    return [json.dumps(info).encode()]

# For Vercel serverless functions
app = application