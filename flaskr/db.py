import os
import psycopg2
from dotenv import load_dotenv, dotenv_values
import click
from flask import current_app, g
import psycopg2.extras

load_dotenv()

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
        dbname="personalblog",
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"))

        g.db.autocommit = True
        g.db.cursor_factory = psycopg2.extras.DictCursor

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    click.echo("Initialising table blog")
    with current_app.open_resource('schema.sql') as f:
        sql_script = f.read().decode('utf8')
        cursor = db.cursor()
        cursor.execute(sql_script)
        cursor.close()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
