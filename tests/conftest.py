from flask_migrate import upgrade, downgrade
import pytest

from app.app import flask_app
from app.models import db


def truncate_all():
    with db.session.begin(subtransactions=True):
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            db.session.execute(table.delete())


def bootstrap_database():
    with flask_app.app_context():
        upgrade()


@pytest.fixture
def app():
    return flask_app


@pytest.fixture(autouse=True)
def database_cleaner():
    try:
        yield
    finally:
        truncate_all()


bootstrap_database()
