web: gunicorn ft_project.wsgi --log-file -
release: python manage.py migrate --run-syncdb
release: python manage.py floodTheDB
