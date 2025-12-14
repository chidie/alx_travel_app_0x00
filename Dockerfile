FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libpq \
    postgresql-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput || true
CMD ["python", "alx_travel_app/manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "alx_travel_app.wsgi:application"]