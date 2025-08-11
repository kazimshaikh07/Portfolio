#!/bin/bash

# Exit on error
set -e

# Install dependencies
pip install -r requirements.txt

# Change to Django project directory
cd portfolio

# Collect static files
python manage.py collectstatic --noinput

# Return to root directory
cd ..