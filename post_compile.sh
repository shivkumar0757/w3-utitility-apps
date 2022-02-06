echo "=> Performing database migrations..."

python manage.py makemigrations

python manage.py migrate