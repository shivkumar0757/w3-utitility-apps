echo "=> Performing database migrations..."
python manage.py migrate
python manage.py makemigrations