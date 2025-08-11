# Simple Django app for Vercel
from django.http import JsonResponse
import os
import sys
import json
import traceback

# Print debug information
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir()}")
print(f"Environment variables: {list(os.environ.keys())}")

# Simple view function
def handler(request, **kwargs):
    """A simple Django view function for Vercel."""
    try:
        # Print request information
        print(f"Request path: {request.path}")
        print(f"Request method: {request.method}")
        
        # Collect environment information
        info = {
            'status': 'ok',
            'message': 'Simple Django app is working',
            'python_version': sys.version,
            'current_directory': os.getcwd(),
            'directory_contents': os.listdir(),
            'environment_variables': list(os.environ.keys()),
            'request_path': request.path,
            'request_method': request.method
        }
        
        # Return a JSON response
        return JsonResponse(info)
    except Exception as e:
        error_message = f"Error in handler: {str(e)}"
        error_traceback = traceback.format_exc()
        print(error_message)
        print(error_traceback)
        
        # Return a JSON error response
        return JsonResponse({
            'status': 'error',
            'message': error_message,
            'traceback': error_traceback,
            'python_version': sys.version,
            'current_directory': os.getcwd(),
            'directory_contents': os.listdir(),
            'environment_variables': list(os.environ.keys())
        }, status=500)