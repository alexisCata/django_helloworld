FROM ubuntu

RUN apt-get update && apt-get install python3-pip python3-dev python3-psycopg2 postgresql postgresql-server-dev-all -y

RUN mkdir -p /usr/local/django_hello_world/

COPY . /usr/local/django_hello_world/

WORKDIR /usr/local/django_hello_world

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000


