from app.app import flask_app
from app.models import db, Comment


def test_created_at_gets_set_on_create():
    with db.session.begin(subtransactions=True):
        comment = Comment()
        db.session.add(comment)

    assert comment.created_at != None

def test_updated_at_gets_changed_on_update():
    with db.session.begin(subtransactions=True):
        comment = Comment()
        db.session.add(comment)

    old_datetime = comment.updated_at
    assert old_datetime != None

    with db.session.begin(subtransactions=True):
        comment.comment_body = 'something_else'

    assert comment.updated_at != old_datetime