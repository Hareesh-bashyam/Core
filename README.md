**Features**

Django 5.2.4

Django REST Framework

JWT Authentication (Access + Refresh Tokens)

PostgreSQL Database

.env support for secret keys and DB credentials

Token blacklisting enabled

Custom accounts app


**Installation & Setup**
1️ Clone the Repository
git clone <repo-url>
cd core

2️ Create & Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate

3️ Install Dependencies
pip install -r requirements.txt

Environment Variables

**Create a .env file in your project root:**

DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=core
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

**PostgreSQL Database Configuration**

The project reads DB configuration from .env:

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


**Running the Project**
Apply Migrations
python manage.py migrate

Create a Superuser
python manage.py createsuperuser

Start the Server
python manage.py runserver


**App runs at:**

http://127.0.0.1:8000/

