#!/bin/bash
# Exit on error
set -e

# Generate a random 50-character Django secret key
generate_key() {
  tr -dc 'a-z0-9!@#$%^&*(-_=+)' </dev/urandom | head -c 50
}

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
  echo "Creating .env file..."
  SECRET_KEY=$(generate_key)
  POSTGRES_PASS=$(generate_key)
  SUPERUSER_PASS=$(generate_key)
  cat > .env <<EOF
# Auto-generated environment file
SECRET_KEY='$SECRET_KEY'
POSTGRES_PASSWORD='$POSTGRES_PASS'
POSTGRES_DB=django
POSTGRES_HOST=db
POSTGRES_USER=django
REDIS_HOST=cache
DEBUG=True
URL=localhost
URL_CRSF=http://localhost
SUPERUSER_USERNAME=
SUPERUSER_EMAIL=
SUPERUSER_PASSWORD='$SUPERUSER_PASS'
EOF

  echo ".env created with secure values."
else
  echo ".env file already exists, skipping generation."
fi

# Run docker compose
docker compose up -d 
