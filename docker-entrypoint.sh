python manage.py migrate
python manage.py collectstatic –noinput
#
touch /home/pyoung/WebDev/django/dockyard/logs/gunicorn.log
touch /home/pyoung/WebDev/django/dockyard/logs/access.log
tail -n 0 -f /home/pyoung/WebDev/django/dockyard/logs/*.log &
#
echo “Starting Gunicorn…”
#exec gunicorn CaaS.wsgi:application \
#    --name CaaS \
#    --bind 0.0.0.0:8000 \
#    --workers 3 \
#    --log-level=info \
#    --log-file=/home/pyoung/WebDev/django/dockyard/logs/gunicorn.log \
#    --access-logfile=/home/pyoung/WebDev/django/dockyard/logs/access.log \
#    “$@”

exec gunicorn CaaS.wsgi:application \
    --name CaaS \
    --bind CaaS.sock \
    --workers 3 \
    --log-level info \
    --log-file /src/gunicorn.log \
    --access-logfile /src/access.log &

exec service nginx start
