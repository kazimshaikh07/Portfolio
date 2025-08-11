#!/usr/bin/env bash

# Exit on error
set -e

echo "Starting Vercel build process..."
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip

# Try to install from requirements-vercel.txt first
if [ -f "requirements-vercel.txt" ]; then
  echo "Installing from requirements-vercel.txt..."
  python -m pip install -r requirements-vercel.txt
else
  echo "Installing from requirements.txt and api/requirements.txt..."
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