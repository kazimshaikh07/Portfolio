#!/usr/bin/env bash

# Exit on error
set -e

# Make script more portable
if [ -z "$BASH_VERSION" ]; then
  exec bash "$0" "$@"
fi

echo "Starting build process..."
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Node version: $(node --version || echo 'Node not available')"
echo "NPM version: $(npm --version || echo 'NPM not available')"

# Ensure we're in the project root
cd "$(dirname "$0")"

# Install dependencies
echo "Installing dependencies..."

# Try different pip commands in case one fails
if command -v pip3 &> /dev/null; then
  echo "Using pip3..."
  pip3 install -r requirements.txt
  pip3 install -r api/requirements.txt
elif command -v pip &> /dev/null; then
  echo "Using pip..."
  pip install -r requirements.txt
  pip install -r api/requirements.txt
else
  echo "Using python -m pip..."
  python -m pip install -r requirements.txt
  python -m pip install -r api/requirements.txt
fi

# Change to Django project directory
echo "Changing to Django project directory..."
cd portfolio

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"

# Return to root directory
cd ..

echo "Build process completed successfully!"