# Simple test handler for Vercel

def handler(request, **kwargs):
    """A simple test handler for Vercel serverless functions."""
    import json
    import os
    import sys
    
    # Collect environment information
    info = {
        'status': 'ok',
        'message': 'Test handler is working',
        'python_version': sys.version,
        'current_directory': os.getcwd(),
        'environment_variables': list(os.environ.keys()),
        'request_path': request.path,
        'request_method': request.method
    }
    
    # Return a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps(info),
        'headers': {
            'Content-Type': 'application/json'
        }
    }