# gunicorn config file

bind = "0.0.0.0:8000"
workers = 3
#worker_class = 'gevent'
chdir = "/django_app"
loglevel = "INFO"

