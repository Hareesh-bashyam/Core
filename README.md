# Core (Django) — Setup & Run

## Features

* Django 5.2.4
* Django REST Framework
* JWT Authentication (Access + Refresh Tokens)
* PostgreSQL Database
* .env support for secret keys and DB credentials
* Token blacklisting enabled
* Custom `accounts` app

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repo-url>
cd core
```

### 2. Create & Activate Virtual Environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (Command Prompt):

```cmd
python -m venv .venv
.venv\Scripts\activate
```

Linux / WSL / macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables (.env)

Create a `.env` file in the project root and add the following values:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=core
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

> Make sure `.env` is listed in `.gitignore` to avoid leaking secrets.

---

## PostgreSQL Database Configuration

The project reads DB config from `.env`. Example `DATABASES` setting in `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", 5432),
    }
}
```

---

## Running the Project

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

The app will be available at:

```
http://127.0.0.1:8000/
```

