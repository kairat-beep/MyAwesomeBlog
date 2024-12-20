# MyAwesomeBlog
The template for my personal blog at kairat-tech.com

# Environment

Install **PostgreSQL**
* Django monolith. Should be installed on the instance.

Install **Redis**. Can be turned off in Settings.py: **Remove Cache** code block.
* [Ubuntu Web Server](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-22-04) , the default Digital Ocean droplet.
*  [Docker](https://hub.docker.com/_/redis) for the development environment.
```
docker run --name django-redis -p  6379:6379 -d redis
```

# Installation
[Follow Instructions for HTTPS-Certbot](https://certbot.eff.org/instructions?ws=nginx&os=snap)
```
git clone https://github.com/kairat-beep/MyAwesomeBlog.git
mv MyAwesomeBlog/* django_project
cd django_project/django_project; mkdir media
chown -R django:django media
chmod -R 755 media
```

## After changes
```
git pull origin main
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
sudo systemctl restart gunicorn.service
sudo systemctl restart nginx
PID=$(systemctl show --value -p MainPID gunicorn.service)
```
# Code Format

**Pre-Commit** python package is used. Format as needed.
Follow Python coding convention.
Fix errors if found`
```
black .
isort .
flake8 .
```

# Backup and Docker DB
```
pg_dump -U django -W -d django -h localhost > outfile
scp -r root@website:/home/django/outfile . #website is in a profile ssh config file
scp -r root@website:/home/django/django_project/django_project/{static,media} .
docker run --name gredis -p 6379:6379 -d  redis redis-server --save 60 1 --loglevel warning
docker run --name  gpostgres -p 5432:5432  -e POSTGRES_PASSWORD="PASSWORD" -e POSTGRES_USER="django" -d postgres
docker exec -i gpostgres psql -U django -d django -e POSTGRES_PASSWORD="PASSWORD" < backup/output
```

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
