# Simplified Django application for Vercel deployment
import json
import os
import sys
import traceback
from http.server import BaseHTTPRequestHandler

# Print debug information
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir()}")
print(f"Environment variables: {list(os.environ.keys())}")

# Simple HTML template for the home page
HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio - Vercel Test</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .success {
            background-color: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .contact-form {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            margin-top: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        .debug-info {
            margin-top: 30px;
            padding: 15px;
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .debug-info pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body>
    <h1>Portfolio - Vercel Test</h1>
    
    <div class="success">
        <p>This is a simplified version of the portfolio site running on Vercel!</p>
    </div>
    
    <div class="contact-form">
        <h2>Contact Form</h2>
        <form method="post" action="/">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone">
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
    </div>
    
    <div class="debug-info">
        <h3>Debug Information</h3>
        <pre>{{debug_info}}</pre>
    </div>
</body>
</html>
"""

# Handler function for Vercel
def handler(request, **kwargs):
    """A simplified handler for Vercel that mimics the portfolio site."""
    try:
        # Print request information
        print(f"Request path: {request.path}")
        print(f"Request method: {request.method}")
        print(f"Request headers: {dict(request.headers)}")
        
        # Collect environment information
        debug_info = {
            'python_version': sys.version,
            'current_directory': os.getcwd(),
            'directory_contents': os.listdir(),
            'environment_variables': list(os.environ.keys()),
            'request_path': request.path,
            'request_method': request.method,
            'vercel_url': os.environ.get('VERCEL_URL', 'Not set'),
            'vercel_env': os.environ.get('VERCEL_ENV', 'Not set')
        }
        
        # Handle different paths
        if request.path.startswith('/static/'):
            # Simplified static file handling
            return {
                'statusCode': 404,
                'body': 'Static file not found',
                'headers': {
                    'Content-Type': 'text/plain'
                }
            }
        elif request.path == '/api/info':
            # API endpoint for debug info
            return {
                'statusCode': 200,
                'body': json.dumps(debug_info),
                'headers': {
                    'Content-Type': 'application/json'
                }
            }
        else:
            # Main page
            success_message = ''
            if request.method == 'POST':
                # Simplified form handling
                success_message = '<div class="success">Message sent successfully! (Demo mode)</div>'
            
            # Render the HTML template
            html_content = HOME_TEMPLATE.replace('{{debug_info}}', json.dumps(debug_info, indent=2))
            if success_message:
                html_content = html_content.replace('<div class="success">', f'{success_message}<div class="success">')
            
            return {
                'statusCode': 200,
                'body': html_content,
                'headers': {
                    'Content-Type': 'text/html'
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
                'directory_contents': os.listdir(),
                'environment_variables': list(os.environ.keys())
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }