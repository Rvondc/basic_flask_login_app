# Flask Simple Login System

A basic Flask web application demonstrating a simple login system with a clean architecture approach, focusing on SOLID principles. This application features user authentication (login, logout) without a persistent database, using an in-memory store for demonstration purposes.

## Features

* User Login with hardcoded credentials (for demonstration).
* User Logout.
* Session Management (using Flask sessions).
* Protected Dashboard page accessible only after login.
* Redirect from root (`/`) based on authentication status.
* Modern, sleek black and white design.
* Clean project structure with separation of concerns:
    * Routes for request handling.
    * Services for business logic.
    * Templates for presentation.

## Folder Structure

The project follows a structured layout to promote maintainability:
```text
project_root/
├── app/                      # Main application package
│   ├── __init__.py           # Application factory
│   ├── routes/               # Route blueprints (main_routes.py, auth_routes.py)
│   ├── services/             # Business logic (auth_service.py)
│   ├── static/               # CSS, JavaScript, images
│   └── templates/            # HTML templates
├── tests/                    # Unit and integration tests
├── config.py                 # Application configuration
├── run.py                    # Script to run the development server
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## Prerequisites

* Python 3.7+
* `pip` (Python package installer)
* A virtual environment tool (like `venv`) is highly recommended.

## Setup and Installation

1.  **Clone the repository (if applicable) or create the project directory:**
    ```bash
    # If cloning:
    # git clone <repository_url>
    # cd <project_directory_name>

    # If starting from scratch, navigate to your project_root
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    ```
    * On Windows:
        ```bash
        venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure your `requirements.txt` file is up-to-date. If starting fresh, manually install Flask: `pip install Flask` and then generate `requirements.txt` using `pip freeze > requirements.txt`)*

4.  **(Optional) Create a `.env` file for environment variables:**
    Copy `.env.example` to `.env` (if you have one) and set your `SECRET_KEY`:
    ```
    SECRET_KEY='your_super_secret_and_unique_key'
    ```
    *If not using `.env` files, the `config.py` has a default `SECRET_KEY`, but it's **strongly recommended** to use a unique one, especially for any deployment.*

## Running the Application

To start the Flask development server:

```bash
python run.py
```

The application will typically be available at ```http://127.0.0.1:5000/```.
Navigating to the root ```/``` will redirect you to ```/auth/login``` if not logged in, or ```/auth/dashboard``` if you are.

## Running Tests

To run the automated tests:

1.  Ensure your virtual environment is activated and dependencies are installed.
2.  Navigate to the `project_root` directory.
3.  Run the tests using Python's `unittest` module:
    ```bash
    python -m unittest discover tests
    ```
    Or, if you have `pytest` installed:
    ```bash
    pytest
    ```

## Key Technologies Used

* **Flask**: A lightweight WSGI web application framework in Python.
* **Jinja2**: A modern and designer-friendly templating language for Python (used by Flask).
* **HTML5 & CSS3**: For structuring and styling the web pages.
* **Python `unittest`**: For writing and running automated tests.