#!/bin/sh

# Exit on error
set -e

echo "Starting Vercel build process with vercel.sh..."
echo "Current directory: $(pwd)"

# Try to find Python
if command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
  echo "Using python3"
else
  PYTHON=python
  echo "Using python"
fi

echo "Python version: $($PYTHON --version)"

# Install dependencies
echo "Installing dependencies..."
$PYTHON -m pip install --upgrade pip

# Try to install from requirements-vercel.txt first
if [ -f "requirements-vercel.txt" ]; then
  echo "Installing from requirements-vercel.txt..."
  $PYTHON -m pip install -r requirements-vercel.txt
else
  echo "Installing from requirements.txt and api/requirements.txt..."
  $PYTHON -m pip install -r requirements.txt
  $PYTHON -m pip install -r api/requirements.txt
fi

# Change to Django project directory
echo "Changing to Django project directory..."
cd portfolio

# Collect static files
echo "Collecting static files..."
$PYTHON manage.py collectstatic --noinput

echo "Build completed successfully!"

# Return to root directory
cd ..