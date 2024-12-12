# Task Management API

A Django-based API for managing tasks. This project is part of the Backend Capstone preparation.


# Authentication Setup

This project uses Django REST Framework to implement API authentication.

## Authentication Methods
1. **JWT Authentication**
   - Generate a token: `POST /api/token/`
   - Refresh a token: `POST /api/token/refresh/`

2. **Token Authentication (Optional)**
   - Generate a token for a user: `python manage.py drf_create_token <username>`

## Testing the API
1. **Obtain a JWT Token**
   - Send a `POST` request to `/api/token/` with the following body:
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

2. **Access Secure Endpoints**
   - Add the following header to requests:
     ```
     Authorization: Bearer your_access_token
     ```

3. **Refresh the Token**
   - Send a `POST` request to `/api/token/refresh/` with the following body:
     ```json
     {
       "refresh": "your_refresh_token"
     }
     ```

---

### **4. Push Your Changes to GitHub**

1. Commit your changes:

   ```bash
   git add .
   git commit -m "Add authentication to API"
