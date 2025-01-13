# Django Photo Sharing App

This project is a full-stack web application built with Django, allowing users to share and manage photos. It features user authentication, CRUD operations for photos, and a responsive front-end using Bootstrap 5.

## Features

- User registration and authentication
- Upload, view, update, and delete photos
- Tag photos and filter by tags
- Responsive design using Bootstrap 5

## Screenshots

Photo List

Photo Detail

Upload Photo

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-photo-sharing-app.git
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Visit `http://localhost:8000` in your browser to view the app.

## Usage

- Register a new account or log in with an existing one
- Upload photos by clicking on "Add a photo" in the navbar
- View all photos on the home page
- Click on a photo to view details, update, or delete it
- Use tags to categorize and filter photos

## Technologies Used

- Django
- Python
- Bootstrap 5
- HTML/CSS





Citations:
[1] https://www.sitepoint.com/django-photo-sharing-app/
