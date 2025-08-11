// vercel.config.js - Configuration for Vercel build
module.exports = {
  // Build configuration
  build: {
    env: {
      // Environment variables for the build
      DJANGO_SETTINGS_MODULE: 'portfolio.settings',
      VERCEL: '1',
      PYTHONPATH: '.:./portfolio',
      DEBUG: 'False'
    }
  },
  // Python configuration
  python: {
    // Python version
    version: '3.11'
  }
};