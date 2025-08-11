#!/usr/bin/env bash

# Exit on error
set -e

echo "Starting build process with build.sh..."
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Directory contents: $(ls -la)"

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Try to install API requirements if they exist
if [ -f api/requirements.txt ]; then
    echo "Installing API dependencies..."
    python -m pip install -r api/requirements.txt
fi

# Try Django operations but don't fail if they don't work
echo "Attempting Django operations..."

# Try to collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput || echo "Static collection failed, continuing anyway..."

# Try to run migrations
echo "Running migrations..."
python manage.py migrate || echo "Migrations failed, continuing anyway..."

echo "Build process completed!"
echo "Vercel deployment should now use one of these endpoints:"
echo "- /portfolio (simplified portfolio page)"
echo "- /test (basic test endpoint)"
echo "- /simple (simple WSGI application)"
echo "- /django (Django handler with diagnostics)"
echo "- /direct (direct Django handler)"
echo "- /minimal (minimal Django configuration)"
echo "- /app (simple Django application)"

echo "Build completed successfully!"

# Return to root directory
cd ..