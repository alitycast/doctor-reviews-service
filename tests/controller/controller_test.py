import json
import pytest

from app.app import flask_app
from app.models import Comment, db
from tests.helpers import COMMENT_DATA, HEADERS


def test_create_http_ok(client):
    response = client.post(
        "/comment",
        data=json.dumps(COMMENT_DATA),
        headers=HEADERS
    )

    assert response.status_code == 200

def test_create_empty_body(client):
    response = client.post(
        "/comment",
        data=json.dumps(""),
        headers=HEADERS
    )
    assert response.status_code == 400

def test_get(client):
    response = client.get(
        "/comment/1",
        headers=HEADERS
    )

    assert response.status_code == 200

def test_put(client):
    response = client.put(
        "/comment/1",
        data=json.dumps({"doctor_id": 2}),
        headers=HEADERS
    )

    assert response.status_code == 200

def test_put_mark_inactive(client):
    response = client.put(
        "/comment/1",
        data=json.dumps({"active": False}),
        headers=HEADERS
    )

    assert response.status_code == 200

def test_put_empty_body(client):
    response = client.put(
        "/comment/1",
        data=json.dumps(""),
        headers=HEADERS
    )

    assert response.status_code == 400
