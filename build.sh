#!/usr/bin/env bash

# Exit on error
set -e

echo "Starting build process with build.sh..."
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -r api/requirements.txt

# Change to Django project directory
echo "Changing to Django project directory..."
cd portfolio

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"

# Return to root directory
cd ..