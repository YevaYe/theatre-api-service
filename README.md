# Theatre API

#### (Do not complete all of tasks)

API service for theatre management written in Django Rest Framework (DRF)

## Installing using GitHub

### Install PostgreSQL and create the database

```sh
git clone <your-github-repo-url>
cd theatre_API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver
```

## Run with docker

### Docker should be installed

```sh
docker-compose build
docker-compose up
```

## Getting Access

* Create a user via `/api/user/register/`
* Get an access token via `/api/user/token/`

## Features

* ~~JWT authenticated~~
* ~~Admin panel `/admin/`~~
* ~~Documentation is located at `/api/doc/swagger/`~~
* ~~Managing orders and tickets~~
* ~~Creating plays with genres, actors~~
* ~~Creating theatre halls~~
* ~~Adding performances~~
* ~~Filtering plays and performances~~
* ~~Docker conteiners~~
