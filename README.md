HeartAI Project
Overview
HeartAI is a project that allows users to upload heart sound recordings, store them in a database, and analyze them using machine learning models. The project features a backend server (using Flask) to handle requests and store data and a frontend interface (using React) for user and doctor interactions.

Prerequisites
Before starting, ensure the following are installed on your computer:

Python 3.x: A programming language used to run the backend server.
Node.js and npm: A platform and package manager used for running the frontend application.
SQLite3: A database used to store information about uploaded heart sound recordings.
Git: A tool for downloading code from repositories.
Quick Start with setup.sh
The setup.sh script simplifies the setup process by installing everything needed to run the project.

1. Clone the Repository
Open a terminal (or command prompt) and run: git clone https://github.com/hmj2000/HeartAi---User-Dashboard.git
 cd HeartAi



2. Run the Setup Script
Ensure that setup.sh is in the project root directory.

Make the script executable (so your computer can run it): chmod +x setup.sh

Run the script: ./setup.sh

What the setup.sh Script Does:
Creates a Python virtual environment and activates it. This environment ensures that all necessary Python packages are installed and used without affecting other projects on your computer.
Installs Python dependencies like Flask (the server framework) and werkzeug (a utility library).
Checks for SQLite3 and installs it if it's missing. SQLite3 is a lightweight database system that stores data in a single file.
Installs Node.js dependencies required for the frontend, such as React components.
Important Note:
The script will show messages about what it is doing. If you see any errors, follow the Troubleshooting section below.

Manual Setup Instructions
If you cannot or prefer not to use setup.sh, you can follow these manual steps:

1. Backend Setup (Flask)
Activate the Python virtual environment: source venv/bin/activate
This ensures that you are using the isolated environment created by setup.sh.

Run the Flask server: python app.py
The Flask server will run on http://localhost:5000. This means your computer is now acting as a server, waiting for requests.

2. Frontend Setup (React)
Navigate to the frontend directory: cd heart-analysis-frontend

Start the React development server: npm start

The React application will open in your web browser at http://localhost:3000. This is the interface users and doctors will interact with.

How to Stop or Restart Backend and Frontend Servers
Sometimes you need to stop or restart the servers if you make changes or run into errors.

Kill Process on Port 5000 (Backend)
If the backend is not running as expected or you need to restart it: lsof -t -i:5000 | xargs kill -9

Explanation: This command finds and forcibly stops any processes using port 5000, which is where the backend server runs.

Kill Process on Port 3000 (Frontend)
If the frontend is not responding or needs to be restarted: lsof -t -i:3000 | xargs kill -9

Explanation: This command does the same as above but for the frontend running on port 3000.

How to Use the Application
Upload a Heart Sound: Open your web browser and go to http://localhost:3000. Use the file upload button to select a heart sound file from your computer and click Upload.

Check Uploads: The file you upload will be saved in the ./uploads folder on your computer and stored in the heart_data.db database. To see the uploaded files and their statuses, use your web browser or terminal to go to: http://localhost:5000/get_recordings/<user_id> Replace <user_id> with the appropriate user ID you are testing with (e.g., exampleUserID).

To-Do for Full Functionality
The project currently includes basic functionalities. Here’s what remains:

Integrate ML Model: Add the actual machine learning model code from heartai.py to analyze uploaded heart sound files.
Update Analysis Results: Implement logic to update the analysis_result in the database with the output from the ML model.
User Authentication: Add secure user login and roles (e.g., user vs. doctor) for access control.
Enhanced Frontend UI: Improve the display of results for better user experience.
Doctor Dashboard: Create a detailed interface for doctors to view patient data and analyses.
Troubleshooting and Tips
Checking the Database: Use sqlite3 commands or a database viewer tool to ensure heart_data.db is being updated.
Common Errors:
Missing Dependencies: Re-run the pip install or npm install commands if you see errors about missing packages.
Port Conflicts: If you get errors about ports being in use, use the kill commands mentioned earlier.
Verify Installation: Run python --version and node --version to ensure Python and Node.js are correctly installed.
Additional Information
To start the backend after setup, run: source venv/bin/activate && python app.py
To start the frontend after setup: cd heart-analysis-frontend && npm start

