# Portfolio Project - Vercel Deployment

## Overview
This is a portfolio website built with Django and deployed on Vercel. The project includes multiple test endpoints to diagnose and resolve deployment issues.

## Deployment Endpoints

The following endpoints are available for testing:

- `/` - Main Django application (may not work if Django configuration issues exist)
- `/portfolio` - Simplified portfolio page that works without Django dependencies
- `/test` - Basic test endpoint that returns system information
- `/simple` - Simple WSGI application test
- `/django` - Django-specific handler with detailed diagnostics
- `/direct` - Direct Django WSGI handler
- `/minimal` - Minimal Django configuration test
- `/app` - Simple Django application test

## Deployment Instructions

1. **Install Vercel CLI**:
   ```
   npm install -g vercel
   ```

2. **Login to Vercel**:
   ```
   vercel login
   ```

3. **Deploy to Vercel**:
   ```
   vercel
   ```

4. **Environment Variables**:
   Make sure to set the following environment variables in your Vercel project settings:
   - `DJANGO_SECRET_KEY`
   - `DEBUG` (set to "False" for production)
   - `ALLOWED_HOSTS` (include your Vercel domain)

## Troubleshooting

If you encounter deployment issues:

1. Check the `/portfolio` endpoint first, which should work regardless of Django configuration
2. Try the various test endpoints to isolate the issue
3. Review Vercel logs for specific error messages
4. Ensure all dependencies are correctly specified in requirements.txt
5. Verify Python version compatibility (3.11 is specified in runtime.txt)

## Project Structure

- `api/` - Contains all Vercel serverless functions
- `portfolio/` - Main Django application
- `vercel.json` - Vercel configuration file
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification