#!/bin/bash

# Ensure the script is executable with: chmod +x setup.sh
# Run the script with: ./setup.sh

echo "Setting up HeartAI project..."

# Backend setup (Python)
echo "Creating a Python virtual environment..."
python3 -m venv venv

echo "Activating the virtual environment..."
source venv/bin/activate

echo "Installing Python dependencies..."
pip install Flask sqlite3 werkzeug

# Check for SQLite3 installation
if ! command -v sqlite3 &> /dev/null
then
    echo "SQLite3 not found. Installing SQLite3..."
    sudo apt-get install sqlite3 -y
fi

echo "Backend setup complete."

# Frontend setup (Node.js)
echo "Setting up frontend..."
cd heart-analysis-frontend

echo "Installing npm dependencies..."
npm install

echo "Frontend setup complete."

# Return to the project root
cd ..

echo "All setup steps complete. You can now run the backend and frontend."
echo "To start the backend, use the virtual environment: source venv/bin/activate && python app.py"
echo "To start the frontend, navigate to 'heart-analysis-frontend' and run: npm start"

