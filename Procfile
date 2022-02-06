release: python manage.py migrate
web: gunicorn w3_utility.wsgi --log-file -

worker: sh -c 'python manage.py crontab add'