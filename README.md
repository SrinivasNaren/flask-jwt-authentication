# Flask JWT Authentication

This is a simple **Flask** web application that demonstrates how to implement **JWT (JSON Web Token) Authentication** for securing API routes. The app includes basic user login functionality and JWT-based authentication to access protected routes.

### Key Features:
- **JWT Authentication**: Protects API routes using JWT tokens.
- **Login Route**: Allows users to log in and obtain a JWT token.
- **Protected Notes Route**: The `/notes` route is protected and can only be accessed with a valid JWT token.

### Technologies Used:
- **Flask**: A lightweight web framework for Python.
- **Flask-JWT-Extended**: Extension for Flask to handle JWT tokens.
- **JSON Web Tokens (JWT)**: For secure authentication.

### How to Run the Project:

1. **Install the Dependencies**:
   First, you need to install the necessary libraries. Run the following command in your terminal or command prompt:
   ```bash
   pip install Flask Flask-JWT-Extended
