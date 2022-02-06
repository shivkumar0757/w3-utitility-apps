# release: python manage.py migrate
web: gunicorn w3_utility.wsgi --log-file -

clock: python staking_status_app/cron.py