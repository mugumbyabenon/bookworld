web: gunicorn --chdir library library.wsgi
celery: -A library.celery worker --pool=solo -l info
celerybeat: celery -A library beat -l info
