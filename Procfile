# release: python manage.py migrate
web: gunicorn w3_utility.wsgi --log-file -

clock: python clock.py

# heroku ps:scale clock=1