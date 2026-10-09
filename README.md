# Swynex API Project Setup
A simple REST API built using Python and Flask.
This project includes a health check endpoint, environment variable configuration using python-dotenv, 
and basic application settings managed through a .env file.

## 📌 Project Overview
The Swenex API project provides a basic Flask application with a health check endpoint
to verify that the API is running successfully.

## Features

* Built with Python and Flask.
* Health check endpoint to verify API availability.
* Environment variable management using python-dotenv.
* Configurable application name, port, debug mode, and secret key.
* .gitignore file to exclude unnecessary files from version control.

##  Project Structure
**Swenex-API-project-setup/**
|
---app.py 
___.env 
---.gitignore 
--- README.md  
---requirements.txt 

## 🛠️ Technologies Used
* Python – Programming language
* Flask – Web framework for building APIs
* python-dotenv – Loads environment variables from the .env file
* Git – Version control

## ⚙️ Prerequisites

* Python 3.13.4 
* pip (Python package installer)
* Git (optional, for version control)

## 🚀 Installation and Setup
1. Clone the Repository
If your project is hosted on GitHub, clone it using:

git clone <your-repository-url>
cd Swenex-API-project-setup
Alternatively, navigate directly to your existing project directory.

## **2. Create a Virtual Environment**

Create an isolated Python environment:

python -m venv venv
Activate the virtual environment.

Windows (Command Prompt):

venv\Scripts\activate
Windows (PowerShell):

.\venv\Scripts\Activate.ps1
Linux/macOS:

source venv/bin/activate

## 3. Install Dependencies

Install the required packages:

pip install -r requirements.txt

or If you have not yet added the dependencies to requirements.txt, include:
flask
python dotenv

## 4. Configure Environment Variables
Create a .env file in the root directory of your project.

Example configuration:

APP_NAME="BACKEND APPLICATION"
SECRETE_KEY="DEBAS"
PORT=8080
DEBUG=True
Environment variable descriptions:

**Variable**	**Description**
APP_NAME:	    Name displayed by the health check endpoint
SECRETE_KEY:	Secret key configured for the Flask application
PORT:	        Port on which the application runs
DEBUG:      	Enables or disables Flask debug mode
Keep your .env file private and do not commit real secrets to Git.


## **5. Run the Application**
Start the Flask application with:

python app.py
The application should be available at:

http://127.0.0.1:5000
The port may differ depending on your .env configuration.

## 🔗 API Endpoints
Health Check
Checks whether the API is responding.
* Endpoint: /health_check
* HTTP Method: GET
* URL: http://127.0.0.1:5000/health_check

EXAMPLE request using postman
http://127.0.0.1:5000/health_check
Example response:

{
  "WELCOME TO MY": "BACKEND APPLICATION"
}
The response value depends on the APP_NAME variable configured in your .env file.

## **Testing with a Browser or API Client**

You can test the health check endpoint using:

A web browser
Postman
curl
Send a GET request to /health_check and verify that the API returns a JSON response.

## 👨‍💻 Author

Project Name: Swenex API Project Setup

Description: A basic Flask API project with environment-based configuration and a health check endpoint.

This project is intended as a starting point for developing and extending REST APIs using Flask.



