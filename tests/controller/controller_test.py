import json
import pytest

from app.app import flask_app
from app.models import db, Comment

comment_data = {
    "doctor_id": 2,
    "comment_body": "This doc was great!",
    "rating": 5,
    "author_id": 3,
    "active": True,
}

headers = {
    'content-type': 'application/json',
    'accept': 'application/json'
}

def test_create_http_ok(client):
    response = client.post(
        '/comment',
        data=json.dumps(comment_data),
        headers=headers
    )

    assert response.status_code == 200

def test_create_empty_body(client):
    response = client.post(
        '/comment',
        data=json.dumps(''),
        headers=headers
    )
    assert response.status_code == 400

def test_get(client):
    response = client.get(
        '/comment/1',
        headers=headers
    )

    assert response.status_code == 200

def test_put(client):
    response = client.put(
        '/comment/1',
        data=json.dumps({"doctor_id": 2}),
        headers=headers
    )

    assert response.status_code == 200

def test_put_mark_inactive(client):
    response = client.put(
        '/comment/1',
        data=json.dumps({"active": False}),
        headers=headers
    )

    assert response.status_code == 200

def test_put_empty_body(client):
    response = client.put(
        '/comment/1',
        data=json.dumps(''),
        headers=headers
    )

    assert response.status_code == 400

# def test_create_email_survey(
#     client,
#     mocker
# ):
#     mock_segment = mocker.patch('app.controllers.Survey.segment_user')
#     mock_segment.return_value = ('thank-you-page', 'email', 'delighted', 0.05, 259200)
#     mock_delighted = mocker.patch('app.controllers.delighted.Person.create')

#     email = "a@omaze.com"
#     user_id=1001
#     order_id = 1

#     node_data = {
#             'campaign_id': 1,
#             'user_email': email,
#             'user_id': user_id,
#             'referrer_url': 'http://omaze.com/referrer',
#             'order_id': order_id,
#             'campaign_type': 'premiere'
#     }

#     response = client.post(
#         '/v0/create',
#         data=json.dumps(node_data),
#         headers={
#             'x-omaze-api-key': '1234',
#             'x-omaze-correlation-id': '192873',
#             'content-type': 'application/json',
#             'accept': 'application/json'
#         }
#     )

#     created_survey = Survey.query.first()

#     property_data = {
#         "survey_id": created_survey.id,
#         "email_delay": 259200,
#         "user": {
#             "id": user_id,
#             "email": email,
#             "order_id": order_id
#         },
#         "segment": {
#             "medium": 'email',
#             "variant": 'thank-you-page',
#             "provider": 'delighted'
#         }
#     }

#     assert response.status_code == 200
#     mock_delighted.assert_called_with(
#         email=email,
#         channel='email',
#         delay=259200,
#         properties=property_data
#     )

# def test_create_bad_api_key(client):
#     response = client.post(
#         '/v0/create',
#         data=json.dumps({
#             'campaign_id': 1,
#             'user_email': 'a@omaze.com',
#             'user_id': 1001,
#             'referrer_url': 'http://omaze.com/referrer',
#             'order_id': 1,
#             'campaign_type': 'premiere'
#         }),
#         headers={
#             'x-omaze-api-key': 'WRONG',
#             'x-omaze-correlation-id': '192873',
#             'content-type': 'application/json',
#             'accept': 'application/json'
#         }
#     )

#     assert response.status_code == 401


# def test_create_nullable_body(client):
#     response = client.post(
#         '/v0/create',
#         data=json.dumps(''),
#         headers={
#             'x-omaze-api-key': '1234',
#             'x-omaze-correlation-id': '192873',
#             'content-type': 'application/json',
#             'accept': 'application/json'
#         }
#     )
#     assert response.status_code == 400


