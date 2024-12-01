import psycopg2
from flask import current_app, g

def get_db_connection():
    if "db" not in g:
        g.db = psycopg2.connect(
            host=current_app.config["DB_HOST"],
            dbname=current_app.config["DB_NAME"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"]
        )
    return g.db

def close_db_connection(e=None):
    db = g.pop("db", None)
    if db:
        db.close()

def init_db(app):
    app.teardown_appcontext(close_db_connection)
