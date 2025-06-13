#!/bin/bash
. .env
# Wait until Postgres is ready
echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h db -p 5432 -U django; do
  sleep 1
done
echo "Postgres is ready!"
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py shell -c "
import os
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username=os.environ['SUPERUSER_USERNAME']).exists():
    User.objects.create_superuser(
        os.environ['SUPERUSER_USERNAME'],
        os.environ['SUPERUSER_EMAIL'],
        os.environ['SUPERUSER_PASSWORD']
    )
"
