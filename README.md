# Swynex API Project Setup

The project is a REST API built using Python and Flask, connected to a PostgreSQL database. It provides endpoints to manage 
patient records through CRUD operations (Create, Read, Update, and Delete).
The API includes API Key Authentication,Incoming request Validation,consistent error responses, basic input validation, 
JSON error responses, database connection handling, and environment-based configuration.
This project includes a health check endpoint, environment variable configuration using python-dotenv, 
and basic application settings managed through a .env file.

## 📌 Project Overview
The Swenex API project provides a basic Flask application with a health check endpoint
to verify that the API is running successfully.

## Features

* Built with Python,Flask and PostgreSql.
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
* PostgreSQL
* Psycopg2
* REST API
* JSON
* API key Authentication

## FEATURES
* Health check endpoint
* PostgreSQL database connectivity test
* Create a patient record
* Retrieve a patient record by ID
* Update patient details
* Delete a patient record
* JSON request validation
* Patient ID, name, department, and appointment date validation
* Custom HTTP 405 error handler
* Database error handling and transaction rollback
* Environment variable configuration using .env
* API key Authentication
* Incoming request validation(Payload Validation)
* Consistent Error Responses

## ⚙️ Prerequisites

* Python 3.13.4 
* pip (Python package installer)
* Git (optional, for version control)
* PostgreSQL

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

pip install Flask python-dotenv psycopg2-binary


pip install -r requirements.txt

or If you have not yet added the dependencies to requirements.txt, include:
flask
python dotenv

## 4. Configure Environment Variables
Create a .env file in the root directory of your project.

Example configuration:


APP_NAME="BACKEND APPLICATION"
SECRET_KEY=DEBAS
API_SECRET_KEY=my_api_key_0000
PORT="4070"
DEBUG="True"
DB_NAME="patient_db"

DB_USER="postgres"
DB_PASSWORD="1122"
HOST="localhost"
DB_PORT="5432"
Environment variable descriptions:

**Variable**	**Description**
APP_NAME:	    Name displayed by the health check endpoint
SECRETE_KEY:	Secret key configured for the Flask application
PORT:	        Port on which the application runs
DEBUG:      	Enables or disables Flask debug mode
API_SECRET_KEY: It is ued for Authentication
HOST:           USED for local Server
DB_USER:        it is used for database user verification
DB_PASSWORD:    It is used for database password verification
keep your .env file private and do not commit real secrets to Git.

## 5. Create the PostgreSQL database

Create a database named patient_db using PostgreSQL or pgAdmin.

Create the patient table using the following SQL:

CREATE TABLE patient (
    patient_id VARCHAR(5) primary key ,
    patient_name VARCHAR(30) NOT NULL,
    department VARCHAR(20) NOT NULL,
    appointment_date VARCHAR(10) NOT NULL,
    transaction_id SERIAL unique
);


## **5. Run the Application**
Start the Flask application with:

python app.py
The application should be available at:

http://127.0.0.1:5000
The port may differ depending on your .env configuration.

## 🔗 API Endpoints
Health Check
Checks whether the API is responding.
Endpoint: /health_check
HTTP Method: GET
URL: http://127.0.0.1:5000/health_check

# API authentication END-POINT

### /add_patient(protected end point)

I have protected this end-point by x-api-key  Authentication.
IF the clent enter the correct API-key with valid data and valid request method then 
access this end point.If the client entered the wrong Api key they the response is Unauthorized Access.Enter a valid API key.

### HTTP METHODS  End-Point **Method_Endpoint_Description**

* GET	        /health_check	        Check API status
* GET	        /test_db	        Test PostgreSQL connectivity
* POST	      /add_patient	         Create a patient record
* GET	      /get_patient	         Retrieve a patient by ID
* PUT	    /update_patient         	Update patient details
* DELETE	/delete_patient	           Delete a patient record

EXAMPLE request using postman
http://127.0.0.1:5000/health_check
Example response:

{
  "WELCOME TO MY": "BACKEND APPLICATION"
}
The response value depends on the APP_NAME variable configured in your .env file.

Sample API Requests
Use Postman to test the following endpoints. Set the request header to:

Content-Type: application/json

1. **Health_Check**
Request

GET http://127.0.0.1:4070/health_check
Example response

{
  "message": "ok",
  "WELCOME TO MY": "SWYNEX Patient API"
}
2**. Test Database Connection**
Request

GET http://127.0.0.1:4070/test_db
Successful response

{
  "status": "success",
  "message": "PostgreSQL connection successful"
}
3. **Create a Patient**
Request

POST http://127.0.0.1:4070/add_patient
Request body

{
  "id": "12345",
  "name": "Rahul Sharma",
  "department": "Cardiology",
  "date": "2026-10-20"
}
The id must be a five-digit numeric string. The appointment date should use the YYYY-MM-DD format when the database column is of type DATE.

Example response

{
  "message": "data inserted successfully",
  "patient_id": "12345",
  "patient_name": "Rahul Sharma",
  "department": "Cardiology",
  "appointment_date": "2026-10-20",
  "transaction_id": 1
}
The transaction ID shown is illustrative; the database generates the actual value.

4. **Retrieve a Patient**
Request

GET http://127.0.0.1:4070/get_patient
Request body

{
  "id": "12345"
}
The endpoint currently expects a JSON body with a GET request. In production APIs, a path parameter or query parameter is generally preferable.

5. **Update a Patient**
Request

PUT http://127.0.0.1:4070/update_patient
Request body

{
  "id": "12345",
  "name": "Rahul Kumar",
  "department": "Neurology",
  "date": "2026-10-22"
}
This request is intended to update an existing patient record.

6. **Delete a Patient**
Request

DELETE http://127.0.0.1:4070/delete_patient
Request body

{
  "id": "12345"
}
This request deletes the matching patient record.

# **Validation and Error Handling**

The API includes basic checks for:

Valid JSON request bodies
Required patient fields
Five-digit numeric patient IDs
Patient name length up to 30 characters
Department name length up to 20 characters
Appointment date length
PostgreSQL database errors
HTTP 405 Method Not Allowed responses
Invalid requests return JSON error messages.

## Learning Outcomes

Through this project, I practised:

Building REST APIs with Flask
Connecting Python applications to PostgreSQL
Executing SQL queries using Psycopg2
Implementing CRUD operations
Validating incoming JSON data
Handling database exceptions and transactions
Managing configuration using environment variables
Testing endpoints using Postman

# Internship Task

Organization: SWYNEX Technologies
Task: Task 2 — Database Integration and CRUD Operations
Project: Patient Management REST API

## **Testing with a Browser or API Client**

You can test the health check endpoint using:

A web browser
Postman
curl
Send a GET request to /health_check and verify that the API returns a JSON response.

## 👨‍💻 Author
Name:Debasis Nayak
Project Name: Swenex API Project Setup
Description: A basic Flask API project with environment-based configuration and a health check endpoint.
This project is intended as a starting point for developing and extending REST APIs using Flask.



