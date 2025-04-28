#!/bin/bash

set -e  # Stop on first error

echo "📦 Setting up Python virtual environment..."

# 1. Create a clean virtual environment
python3 -m venv venv

# 2. Activate the venv
source venv/bin/activate

# 3. Upgrade pip (important!)
pip install --upgrade pip

# 4. Install required libraries
pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2

# 5. Debug: show Python version and installed packages
echo "🐍 Python being used:"
which python
python --version

echo "📚 Installed packages:"
pip list

# 6. Now run your app
echo "🚀 Running your app..."
python ui.py

