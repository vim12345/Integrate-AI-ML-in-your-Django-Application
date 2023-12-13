# Django API Documentation

This documentation provides details about the endpoints available in the Django app, their purposes, required parameters, and expected responses.

## Table of Contents
1. [User Authentication](#user-authentication)
   - [1.1 Login](#11-login)
   - [1.2 Register](#12-register)

2. [Customized REST APIs](#customized-rest-apis)
   - [2.1 CRUD Operations](#21-crud-operations)

3. [Text Completion and Image Recognition](#text-completion-and-image-recognition)
   - [3.1 Generate Product Description](#31-generate-product-description)
   - [3.2 Image Recognition](#32-image-recognition)

---

## 1. User Authentication

### 1.1 Login

- **Endpoint**: `/api/login/` (POST)
- **Purpose**: Allows users to log in and retrieve an authentication token.
- **Required Parameters**:
  - `username`: User's username
  - `password`: User's password
- **Expected Response**:
  - Successful login: `{ "token": "<user_authentication_token>", "user_id": <user_id> }`
  - Invalid credentials: `{ "error": "Invalid username or password" }`

### 1.2 Register

- **Endpoint**: `/api/register/` (POST)
- **Purpose**: Allows users to register an account and obtain an authentication token.
- **Required Parameters**:
  - `username`: Desired username for registration
  - `password`: User's password for registration
- **Expected Response**:
  - Successful registration: `{ "token": "<user_authentication_token>", "user_id": <user_id> }`
  - Username taken or missing credentials: `{ "error": "Username is already taken" }`, `{ "error": "Both username and password are required" }`

---

## 2. Customized REST APIs

### 2.1 CRUD Operations

- **Endpoint**: `/api/crud-operations/` (GET, POST)
- **Purpose**: Allows users to perform CRUD operations on certain resources.
- **Required Parameters**:
  - GET: None
  - POST: Data to create a new resource
- **Expected Response**:
  - GET: Returns a list of existing resources
  - POST: Returns the created resource details or errors if validation fails

---

## 3. Text Completion and Image Recognition

### 3.1 Generate Product Description

- **Endpoint**: `/api/api-3/` (POST)
- **Purpose**: Generates a product description based on the provided title and extracts keywords for SEO improvement.
- **Required Parameters**:
  - `title`: Title of the product
- **Expected Response**:
  - `{ "description": "<generated_product_description>", "keywords": ["keyword1", "keyword2"] }`

### 3.2 Image Recognition

- **Endpoint**: `/api/api-4/` (POST)
- **Purpose**: Takes an image as input and returns keywords extracted from the image (text, facial expression, objects, etc.).
- **Required Parameters**:
  - `image`: Image file uploaded through Postman
- **Expected Response**:
  - `{ "keywords": ["keyword1", "keyword2"] }`

---

Feel free to customize this documentation based on your specific API implementation and requirements.
