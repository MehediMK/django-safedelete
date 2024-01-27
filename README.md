# Django Library Management System with Django Soft-Delete functionality

This project demonstrates the implementation of a Library Management System using Django, incorporating soft delete functionality through the django-safedelete package. It includes multiple models, a Django REST Framework (DRF) API, and basic CRUD operations.

## Project Structure

- **library_project**: Django project directory.
- **library**: Django app containing models, views, serializers, and URLs.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/MehediMK/django-safedelete.git
    cd library_project
    ```

2. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
    python3 -m venv venv

    # Activate virtual environment (Linux/Mac)
    source venv/bin/activate

    # Activate virtual environment (Windows)
    venv\Scripts\activate

   ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7.  To load dummy data which was existing in fixtures directory
   ```bash
    python manage.py loaddata authors.json
    python manage.py loaddata books.json
   ```

8. Access the Django admin interface at `http://127.0.0.1:8000/admin/` to add authors and books.
---
## Docker Instructions

To run the project using Docker, follow these steps:

1. Make sure Docker is installed on your system. If not, you can download and install Docker from [here](https://www.docker.com/get-started).

2. Build the Docker image and start the container:

    ```bash
    docker-compose up --build
    ```

3. Access the Django project at `http://localhost:8000`.
---
## Features

- **Soft Delete**: Utilizes django-safedelete to implement soft delete functionality, allowing records to be marked as deleted without physically removing them from the database.
- **RESTful API**: Provides CRUD operations for authors and books through a DRF API.
- **Admin Interface**: Allows easy management of library data through the Django admin interface.
- **Fixture Data**: Included fixture files provide sample data for authors and books to quickly populate the database.

## Usage

### Django Admin

1. Create superuser: `python manage.py createsuperuser`
2. Visit `http://127.0.0.1:8000/admin/`
3. Log in with superuser credentials.
4. Add authors and books through the admin interface.

### RESTful API

- **Authors**: `http://127.0.0.1:8000/api/authors/`
- **Books**: `http://127.0.0.1:8000/api/books/`

## Contributors
Feel free to customize this README file further based on your project's specific details and requirements!
- [Your Name](https://github.com/your-username)

