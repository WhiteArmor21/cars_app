# Cars app Dockerized backend
## Launch instructions:
- in core catalog (contains files : Dockerfile, docker-compose.yml, manage.py,...)
- use command "docker-compose up -d --build" for launch in dev mode.
- use command "docker-compose -f docker-compose.prod.yml up -d --build" for launch in prod mode
- since that moment, the service will be available by url "http://localhost:8000/"
To delete containers use:
- "docker-compose down -v"
