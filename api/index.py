import os
import sys
import traceback

try:
    # Import the WSGI application from our custom wsgi module
    from api.wsgi import application
    
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
    
    # Fallback to a simple response if Django fails to load
    def handler(request, **kwargs):
        """Fallback handler when Django fails to load."""
        import json
        from http.server import BaseHTTPRequestHandler
        
        class SimpleHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error_info = {
                    'status': 'error',
                    'message': f'Django application failed to load: {str(e)}',
                    'traceback': traceback.format_exc()
                }
                self.wfile.write(json.dumps(error_info).encode())
                return
        
        return SimpleHandler(request, request.client_address, None)

