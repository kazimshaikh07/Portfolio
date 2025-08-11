#!/bin/bash

# Exit on error
set -e

echo "Starting build process..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
pip install -r api/requirements.txt

# Change to Django project directory
echo "Changing to Django project directory..."
cd portfolio

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Return to root directory
cd ..

echo "Build process completed successfully!"