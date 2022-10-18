#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "DB not yet run..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "DB did run."
fi

python manage.py flush --no-input
python manage.py makemigrations products
python manage.py migrate

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL \
        --password $DJANGO_SUPERUSER_PASSWORD
fi

exec "$@"