# BMW Shop

A web application for managing BMW parts and services.

## Features

- Customer Portal:
  - Browse BMW series and models
  - Select parts and accessories
  - Place orders
  - View order history
  - Leave feedback

- Admin Dashboard:
  - Manage BMW series
  - Manage parts inventory
  - View orders
  - Track customer records
  - Monitor sales statistics

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd bmw_shop
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the application:
- Main website: http://127.0.0.1:8000/
- Custom Admin Dashboard: http://127.0.0.1:8000/dashboard/
- Django Admin Interface: http://127.0.0.1:8000/django-admin/

## VSCode Setup

1. Install recommended VSCode extensions:
   - Python
   - Django
   - SQLite Viewer

2. Open the project in VSCode:
```bash
code .
```

3. Select Python Interpreter:
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your virtual environment (venv)

4. Debug Configuration:
   - Press `Ctrl+Shift+D`
   - Create a launch.json file for Django
   - Use the following configuration:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
            "justMyCode": true
        }
    ]
}
```

## Usage

1. Start the server using VSCode:
   - Press `F5` or click the green play button
   - The server will start in debug mode

2. Access the website:
   - Open http://127.0.0.1:8000/ in your browser
   - Access custom admin dashboard at http://127.0.0.1:8000/dashboard/
   - Access Django admin at http://127.0.0.1:8000/django-admin/

3. Development:
   - Use VSCode's integrated terminal
   - Django development server auto-reloads on file changes
   - Set breakpoints for debugging
   - Use SQLite Viewer to inspect the database

## Project Structure

```
bmw_shop/
├── app/                    # Main application
│   ├── migrations/        # Database migrations
│   ├── static/           # Static files (CSS, JS)
│   ├── templates/        # HTML templates
│   ├── admin.py         # Admin interface
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   └── urls.py          # URL routing
├── bmw_shop/             # Project settings
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
``` 