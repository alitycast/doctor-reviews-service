# doctor-reviews-service

run app - FLASK_APP=app.app:flask_app python -m flask run


Create database migration
FLASK_APP=app.app:flask_app python -m flask db init - don't do?
FLASK_APP=app.app:flask_app python -m flask db migrate
FLASK_APP=app.app:flask_app python -m flask db upgrade

login to db
mysql -uroot -hlocalhost



TODO:
Controller functionality
Optimize?
Tests
Readme
remove unsued directories/code/imports
check requirements again

POST
curl -X POST http://127.0.0.1:5000/comment -H "Content-Type: application/json" -d '{"doctor_id": 1, "comment_body": "so so", "rating": 5, "author_id": 2}'

GET
curl -X GET http://127.0.0.1:5000/comment/1 -H "Content-Type: application/json"