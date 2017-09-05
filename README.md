# cas_example
A CAS example including an authentication server and two apps

## Run
```sh
docker-compose up -d
docker-compose exec cas_server python manage.py migrate
docker-compose exec cas_app1 python manage.py migrate
docker-compose exec cas_server python manage.py createsuperuser
```

Open http://172.28.1.2 and http://172.28.1.3
