# Bogie_Api


# Backend Assignment – Sarva Suvidhan Pvt. Ltd.

## Project Overview

This project contains the implementation of two backend API endpoints using FastAPI and PostgreSQL. The APIs are based on the requirements provided in the Postman collection and Swagger documentation by Sarva Suvidhan Pvt. Ltd.

## Tech Stack

- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- pgAdmin (for DB visualization)
- Render (for PostgreSQL hosting)

## API Endpoints Implemented

### 1. Bogie Checksheet API
- *Method*: POST  
- *URL*: /api/forms/bogie-checksheet  
- *Functionality*: Accepts bogie inspection data, validates it, and stores it in the PostgreSQL database.  

### 2. Wheel Specifications API
- *Method*: POST  
- *URL*: /api/forms/wheel-specs  
- *Functionality*: Submits wheel measurement data with required details and stores it in the database.  

## Features

- Pydantic validation for structured input
- JSONB fields used for nested data
- PostgreSQL database integration
- Environment variable management using .env file
- Modular and clean folder structure
- Postman-tested endpoints with sample requests/responses
