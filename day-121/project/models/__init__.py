from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext

db = SQLAlchemy()

def init_db():
    """Clear existing data and create new tables."""
    db.drop_all()
    db.create_all()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    db.init_app(app)
    # db = SQLAlchemy(app)
    print("models.init_app ===> app.config SQLALCHEMY_DATABASE_URI:", app.config.get("SQLALCHEMY_DATABASE_URI", None))
    # db.init_app(app)
    app.cli.add_command(init_db_command)
    return db