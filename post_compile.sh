echo "=> Performing database migrations..."

python manage.py makemigrations

python manage.py migrate

python manage.py crontab add

python manage.py crontab show