import json

from app.app import flask_app
from app.models import db, Comment
from tests.helpers import COMMENT_DATA, HEADERS


def test_create(client):
    response = client.post(
        "/comment",
        data=json.dumps(COMMENT_DATA),
        headers=HEADERS
    )
    assert response.status_code == 200

    comment = Comment.query.order_by(Comment.id.desc()).first()

    assert COMMENT_DATA == {
        "doctor_id": comment.doctor_id,
        "comment_body": comment.comment_body,
        "rating": comment.rating,
        "author_id": comment.author_id,
        "active": comment.active
    }

    assert isinstance(json.loads(response.data), list)
    assert len(json.loads(response.data)) == 5

def test_update(client):
    response = client.post(
        "/comment",
        data=json.dumps(COMMENT_DATA),
        headers=HEADERS
    )

    assert response.status_code == 200

    comment = Comment.query.order_by(Comment.id.desc()).first()

    response = client.put(
        "/comment/{}".format(comment.id),
        data=json.dumps({"active": False}),
        headers=HEADERS
    )

    assert response.status_code == 200

    updated_comment = Comment.query.get(comment.id)

    assert updated_comment.active == False

