# MyAwesomeBlog
The template for my personal blog at kairat-tech.com

# Environment
Digital Ocean Hosting ~6$.
* [Ubuntu Web Server](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-22-04) , the default Digital Ocean droplet.
* * Install **PostgreSQL**
* * Install **Redis**. Can be turned off in Settings.py: **Remove Cache** code block.

Docker version
*  [Docker Web](https://hub.docker.com/layers/library/python/3.13-slim/images/sha256-8bc85201ccb77449e1c0ec24b5caeaf343a3842da11c3a6921afc5c196170791) is python-3.13.slim for the development environment.
*  [Docker Postgres](https://hub.docker.com/_/postgres) for the development environment.
*  [Docker Redis](https://hub.docker.com/_/redis) for the development environment.

# Installation
## Local Environment
Generates .env file with keys for local development. The script starts Python slim, Redis, and Postgres docker images. Postgres uses volumes to preserve the state.
```
chmod +x run.sh run_django.sh
./run.sh
```

## Deployment. 2Gb is required for docker deployment.
Reuse the .env file generated in development version
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
Fix errors if found
```
black .
isort .
flake8 .
```

# Backup and Docker DB
```
docker exec db pg_dump -U django -W -d django -h db > outfile
scp -r root@website:/home/django/outfile . #website is in a profile ssh config file
scp -r root@website:/home/django/django_project/django_project/{static,media} .
docker exec -i db psql -U django -d django -e POSTGRES_PASSWORD="PASSWORD_GOES_HERE" < backup/output
```

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
