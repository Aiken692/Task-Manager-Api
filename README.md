# Task Management API
<img width="781" alt="image" src="https://github.com/user-attachments/assets/fac41ba9-408b-4caf-9f5f-744a281f0e46" />


A Django-based API for managing tasks. This project is part of the Backend Capstone preparation.

## Authentication Setup
## Authentication Setup

This project uses Django REST Framework to implement API authentication.

## Authentication Methods


1. **JWT Authentication**


   - Generate a token: `POST /api/token/`
   - Refresh a token: `POST /api/token/refresh/`

2. **Token Authentication (Optional)**


   - Generate a token for a user: `python manage.py drf_create_token <username>`

## Testing the API


1. **Obtain a JWT Token**

   - Send a `POST` request to `/api/token/` with the following body in JSON format:

     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```

   - Example Response:


     ```json
     {
       "access": "your_access_token",
       "refresh": "your_refresh_token"
     }
     ```

   - **Explanation:**
     - The request retrieves an access token and a refresh token upon successful authentication.
     - Store these tokens securely, as they will be used to access authorized API endpoints.

   - **Explanation:**
     - The request retrieves an access token and a refresh token upon successful authentication.
     - Store these tokens securely, as they will be used to access authorized API endpoints.

2. **Access Secure Endpoints**

   - Add the following header to your requests to access secure API endpoints:

     ```
     Authorization: Bearer your_access_token
     ```

   - **Explanation:**
     - The `Authorization` header indicates that you are using Bearer token authentication.
     - Replace `your_access_token` with the actual access token obtained in step 1.

3. **Refresh the Token**

   - Send a `POST` request to `/api/token/refresh/` with the following body in JSON format:

     ```json
     {
       "refresh": "your_refresh_token"
     }
     ```

   - **Explanation:**
     - Use the refresh token to obtain a new access token when the current one expires.
     - This helps maintain uninterrupted API access during extended sessions.

---

### Common API Scenarios

#### Scenario 1: Retrieve Task List

* **Request Method:** GET
* **Endpoint:** /tasks/
* **Authorization:** Bearer Token
* **Response:**
    * Status Code: 200 OK
    * Response Body:

      ```json
      [
        {
          "id": 1,
          "title": "New Task",
          "description": "This is a new task.",
          "is_complete": false,
          "deadline": null,
          "created_at": "2024-12-21T16:39:07.301495Z",
          "updated_at": "2024-12-21T16:39:07.301547Z",
          "user": 1
        }
      ]
      ```

    * Possible Errors:
        * 401 Unauthorized: If the token is invalid or expired.
        * 403 Forbidden: If the user doesn't have permission to access the task list.

* **Explanation:**
    - This request retrieves a list of all tasks for the authenticated user.
    - The response includes details like task ID, title, description, completion status, deadline, creation/update timestamps, and the associated user ID.

#### Scenario 2: Create a New Task

* **Request Method:** POST
* **Endpoint:** /tasks/create/
* **Authorization:** Bearer Token
* **Body:**

  ```json
  {
    "title": "New Task",
    "description": "This is a new task.",
    "user": 1
  }
