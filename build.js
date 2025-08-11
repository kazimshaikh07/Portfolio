// build.js - JavaScript fallback build script for Vercel
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function runCommand(command) {
  console.log(`Running: ${command}`);
  try {
    execSync(command, { stdio: 'inherit' });
    return true;
  } catch (error) {
    console.error(`Error executing command: ${command}`);
    console.error(error.message);
    return false;
  }
}

function main() {
  console.log('Starting JavaScript build process...');
  console.log(`Current directory: ${process.cwd()}`);
  
  // Find Python executable
  let pythonCmd = 'python';
  try {
    execSync('python3 --version', { stdio: 'ignore' });
    pythonCmd = 'python3';
  } catch (error) {
    console.log('python3 not found, using python');
  }
  
  console.log(`Using Python command: ${pythonCmd}`);
  runCommand(`${pythonCmd} --version`);
  
  // Install dependencies
  console.log('Installing dependencies...');
  runCommand(`${pythonCmd} -m pip install --upgrade pip`);
  
  // Try to install from requirements-vercel.txt first
  if (fs.existsSync('requirements-vercel.txt')) {
    console.log('Installing from requirements-vercel.txt...');
    runCommand(`${pythonCmd} -m pip install -r requirements-vercel.txt`);
  } else {
    console.log('Installing from requirements.txt and api/requirements.txt...');
    runCommand(`${pythonCmd} -m pip install -r requirements.txt`);
    runCommand(`${pythonCmd} -m pip install -r api/requirements.txt`);
  }
  
  // Change to Django project directory
  console.log('Changing to Django project directory...');
  process.chdir('portfolio');
  
  // Collect static files
  console.log('Collecting static files...');
  runCommand(`${pythonCmd} manage.py collectstatic --noinput`);
  
  console.log('Build completed successfully!');
  
  // Return to root directory
  process.chdir('..');
}

main();