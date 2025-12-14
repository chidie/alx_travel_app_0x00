# alx_travel_app

A Django + Django REST Framework project containerized with Docker, designed to manage travel listings, bookings, and reviews. Includes a custom user model with role-based access (`guest`, `host`, `admin`).

---

## Features
- Custom `User` model with roles (`guest`, `host`, `admin`)
- Models for `Listing`, `Booking`, and `Review`
- REST API endpoints with DRF viewsets
- PostgreSQL database + Redis for background tasks
- Dockerized setup with `docker-compose`
- Django Admin interface for managing data
- Seed script for populating sample data

---

## Tech Stack
- **Backend**: Django 5, Django REST Framework
- **Database**: PostgreSQL 15 (alpine)
- **Cache/Queue**: Redis 7
- **Containerization**: Docker, Docker Compose
- **Language**: Python 3.11 (alpine)

---

## Project Structure
```bash
    alx_travel_app/ 
    │ ├── alx_travel_app/ # Django project root 
    │ ├── settings.py 
    │ ├── urls.py 
    │ └── manage.py 
    │ ├── listings/ # Listings app 
    │ ├── models.py # User, Listing, Booking, Review 
    │ ├── serializers.py # DRF serializers 
    │ ├── views.py # DRF viewsets 
    │ ├── admin.py # Admin registration 
    │ └── management/commands/seed.py # Seed script 
    │ ├── Dockerfile 
    ├── docker-compose.yml 
    └── requirements.txt
```


---

## ⚙️ Setup

### 1. Clone and build
```bash
git clone <repo-url>
cd alx_travel_app
docker compose up --build

```bash
    docker compose exec app python manage.py makemigrations
    docker compose exec app python manage.py migrate

    docker compose exec app python manage.py createsuperuser
    docker compose exec app python manage.py seed

```

🧑Models
```bash
    User
    user_id (UUID, PK)
    first_name, last_name, email (unique)
    role (guest, host, admin)
    created_at
    Listing
    listing_id (UUID, PK)
    user (FK → User)
    title, description, price, location
    created_at

    Booking
    booking_id (UUID, PK)
    listing (FK → Listing)
    user (FK → User)
    status (pending, confirmed, canceled)
    start_date, end_date, total_price
    created_at

    Review
    review_id (UUID, PK)
    listing (FK → Listing)
    user (FK → User)
    rating (1–5)
    comment
    created_at
```
To seed:
```bash
    docker compose exec app python manage.py seed
```
### Create the project & virtualenv (why: isolation, reproducibility)
```bash
   mkdir alx_travel_app && cd alx_travel_app
   python -m venv .venv
   .venv\Scripts\Activate.ps1
```

### Create requirements.txt and install packages (why: repeatable installs)
```bash
    Django>=4.2
    djangorestframework
    django-cors-headers
    django-environ
    drf-yasg
    celery
    pika            # (for RabbitMQ python client directly; optional)
    mysqlclient     # or PyMySQL (mysqlclient is common)
```

### Install the libraries
```bash
   pip install -r requirements.txt
```

### Start the Django project & app
```bash
    django-admin startproject alx_travel_app .
    python manage.py startapp listings

### Configure settings.py — REST framework, CORS, MySQL via environment variables
```bash
   INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "rest_framework",
    "corsheaders",
    "drf_yasg",

    # local apps
    "listings",
] 
```
### Configure Celery
```bash
    python -m celery -A alx_travel_app worker --loglevel=info
```

### Migrate and runserver
```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser   # optional
    python manage.py runserver
```

> Note: 
```bash
    docker compose exec app python alx_travel_app/manage.py migrate
    docker compose down --remove-orphans # remove orphaned containers
    docker compose build --no-cache # If dockerfile is changed, rebuild without cache
```


> Note: When AUTH_USER_MODEL points at your listings.User, Django will treat that model as the project user model (so you won't have both auth.User and listings.User active for authentication). That removes the duplicate reverse accessors that caused the SystemCheckError.
```bash
# Keyerror: listings.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'listings.User.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
#         HINT: Add or change a related_name argument to the definition for 'listings.User.user_permissions' or 'auth.User.user_permissions'.
```
