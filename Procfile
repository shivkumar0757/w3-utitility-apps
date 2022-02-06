# release: python manage.py migrate
web: gunicorn w3_utility.wsgi --log-file -

worker: python staking_status_app/cron.py