# E-Library API System
This project implements an E-Library API using FastAPI. It allows users to manage books, users, and borrowing operations in an online library system.

## Features
- **User Management**:
  - Create, read, update, and delete users.
  - Deactivate users.

- **Book Management**:
  - Create, read, update, and delete books.
  - Mark books as unavailable.

- **Borrow Operations**:
  - Borrow and return books.
  - View borrowing records by user or globally.

## Requirements
- Python
- fastapi
- uvicorn
- pytest

## Installation
1. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

## Running the Application
   Start the FastAPI application using `uvicorn`:
   uvicorn main:app --reload

## Running Tests
1. Run the test cases with `pytest`: 
   pytest test_e_library_api.py
   

## Usage
- Use the Swagger UI to test endpoints interactively.
- Ensure to start the application and create initial users and books before testing borrowing operations.

