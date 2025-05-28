# Sanjeevani Hospital Management System

A comprehensive hospital management system built with Flask RESTful API backend and a web frontend.

## Features

- Patient Management
- Doctor Management
- Appointment Scheduling
- Token Generation System
- User-friendly Interface

## Tech Stack

- **Backend**: Python Flask RESTful API
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/sanjeevani.git
   cd sanjeevani
   ```

2. Install the required dependencies:
   ```
   pip install flask flask-restful
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Access the application at:
   ```
   http://127.0.0.1:9000
   ```

## API Endpoints

### Patient
- `GET /patient` - List all patients
- `POST /patient` - Add a new patient
- `GET /patient/<id>` - Get patient details
- `PUT /patient/<id>` - Update patient details
- `DELETE /patient/<id>` - Delete a patient

### Doctor
- `GET /doctor` - List all doctors
- `POST /doctor` - Add a new doctor
- `GET /doctor/<id>` - Get doctor details
- `PUT /doctor/<id>` - Update doctor details
- `DELETE /doctor/<id>` - Delete a doctor

### Appointment
- `GET /appointment` - List all appointments
- `POST /appointment` - Schedule a new appointment
- `GET /appointment/<id>` - Get appointment details
- `PUT /appointment/<id>` - Update appointment details
- `DELETE /appointment/<id>` - Cancel an appointment

### Token
- `GET /token` - List all tokens
- `POST /token` - Generate a new token
- `GET /token/<id>` - Get token details
- `PUT /token/<id>` - Update token details
- `DELETE /token/<id>` - Delete a token

## Database Schema

The application uses SQLite with the following tables:
- `patient` - Stores patient information
- `doctor` - Stores doctor information
- `appointment` - Manages appointments between patients and doctors

## License

This project is licensed under the MIT License.

## Author

Tushar Borole 