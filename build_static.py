#!/usr/bin/env python

import os
import subprocess
import sys

def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, check=True)
    return result

def main():
    print("Starting Python build process...")
    print(f"Current directory: {os.getcwd()}")
    print(f"Python version: {sys.version}")
    
    # Install dependencies
    print("Installing dependencies...")
    run_command(f"{sys.executable} -m pip install --upgrade pip")
    
    # Try to install from requirements-vercel.txt first
    if os.path.exists("requirements-vercel.txt"):
        print("Installing from requirements-vercel.txt...")
        run_command(f"{sys.executable} -m pip install -r requirements-vercel.txt")
    else:
        print("Installing from requirements.txt and api/requirements.txt...")
        run_command(f"{sys.executable} -m pip install -r requirements.txt")
        run_command(f"{sys.executable} -m pip install -r api/requirements.txt")
    
    # Change to Django project directory
    print("Changing to Django project directory...")
    os.chdir("portfolio")
    
    # Collect static files
    print("Collecting static files...")
    run_command(f"{sys.executable} manage.py collectstatic --noinput")
    
    print("Build completed successfully!")
    
    # Return to root directory
    os.chdir("..")

if __name__ == "__main__":
    main()