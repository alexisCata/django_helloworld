from django.http import HttpResponse
import os
import psycopg2


def index(request):
    db_host = os.environ.get('DB_HOST', "localhost")
    conn = psycopg2.connect(host=db_host,
                            database="my_db",
                            user="my_db_user1",
                            password="My_db_pass1")
    cur = conn.cursor()
    cur.execute("SELECT version()")
    db_version = cur.fetchone()
    cur.execute("SELECT datname from pg_database")
    db_dbs = cur.fetchall()

    return HttpResponse("Hello, world!!!!!! ----- DB Host: {} ----- DB Version: {} ----- DB databases: {}"
                        .format(db_host, db_version, db_dbs))
