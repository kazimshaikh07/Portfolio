# Minimal URL configuration for testing
from django.http import JsonResponse
from django.urls import path
import os
import sys

# Simple view that returns system information
def debug_view(request):
    """A simple view that returns system information."""
    return JsonResponse({
        'status': 'ok',
        'message': 'Minimal Django is working',
        'python_version': sys.version,
        'current_directory': os.getcwd(),
        'environment_variables': list(os.environ.keys()),
        'request_path': request.path,
        'request_method': request.method,
        'request_headers': dict(request.headers),
    })

# URL patterns
urlpatterns = [
    path('', debug_view, name='debug'),
]