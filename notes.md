# Django Setup and Workflow

## Installing Django

### Option 1: Using `pip`
```bash
pip install django  # Installs Django globally
```

### Option 2: Using `pipenv` (Recommended)
```bash
pipenv install django  # Installs Django in the project folder
```

## Setting Up `pipenv`

1. Install `pipenv`:
   ```bash
   pip install pipenv
   ```

2. Verify installation:
   ```bash
   pip show pipenv
   pipenv --version
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

## Starting a Django Project

1. View available Django admin commands:
   ```bash
   django-admin
   ```

2. Start a new Django project:
   ```bash
   django-admin startproject storefront .
   ```

3. Run the Django project:
   ```bash
   python manage.py runserver  # Runs on the default port (8000)
   python manage.py runserver 7000  # Runs on a custom port (7000)
   ```

## Setting Python Interpreter in VS Code

1. Find the virtual environment path:
   ```bash
   pipenv --venv
   ```

2. Copy the path and append `\Scripts\python.exe` (e.g., `C:\Users\charith\.virtualenvs\storefront-JshKXDAk\Scripts\python.exe`).

3. Set the Python interpreter in VS Code:
   - Press `Ctrl + P`.
   - Search for `Python: Select Interpreter`.
   - Choose `Enter Interpreter Path` and paste the path.

## VS Code Terminal Shortcuts

- Open terminal: Ctrl + ` or J 
- Clear terminal: Ctrl + L

## Creating a Django App

1. Create a new app:
   ```bash
   python manage.py startapp playground
   ```

2. Key files and their purposes:

   - **`migrations/`**: Tracks and applies database migrations (e.g., generating database tables).
   - **`admin.py`**: Customizes the Django admin interface.
   - **`apps.py`**: Configures the app.
   - **`models.py`**: Defines model classes to interact with the database.
   - **`views.py`**: Handles requests and returns responses.

---
