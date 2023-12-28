# FastAPI Sample Project

This is a simple FastAPI project with CRUD (Create, Read, Update, Delete) operations using an in-memory database.



## Introduction

This project demonstrates a basic FastAPI application with in-memory database operations. It provides API endpoints for creating, reading, updating, and deleting items.

## Install Dependencies:

pip install fastapi
pip install uvicorn



## Run the Application:

uvicorn main:app --reload


## Usage
Open your web browser and go to http://127.0.0.1:8000/docs to access the interactive Swagger documentation.
Use the provided API endpoints for CRUD operations on items.

## Endpoints
Read Item:

Endpoint: /items/{item_id}
Method: GET
Retrieves information about a specific item.
Create Item:

Endpoint: /items/{item_id}
Method: POST
Creates a new item.
Update Item:

Endpoint: /items/{item_id}
Method: PUT
Updates information about an existing item.
Delete Item:

Endpoint: /items/{item_id}
Method: DELETE
Deletes an existing item.
