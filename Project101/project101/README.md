# Project Title: Project101

## Overview
Project101 is a Django web application that includes a user registration feature through the `signapp` application. This project allows users to sign up by providing their personal information, which is managed through the Django admin interface.

## Features
- User registration with validation
- Admin interface for managing user registrations

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd project101
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser to access the admin interface:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the admin interface at `http://127.0.0.1:8000/admin` and log in with the superuser credentials.
- Manage user registrations through the `SignUpRegistration` model in the admin panel.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.