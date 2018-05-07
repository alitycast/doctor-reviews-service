from flask import abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from app import flask_app
from models import db, Comment, Doctor

@flask_app.route("/comment/<int:comment_id>")
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)

    data = comment.format()

    response = jsonify(data)
    response.status_code = 200

    return response


@flask_app.route("/comment", methods=["POST"])
def create_comment():
    if not request.json:
        abort(400)

    with db.session.begin(subtransactions=True):
        comment = Comment(
            doctor_id=request.json.get("doctor_id"),
            comment_body=request.json.get("comment_body"),
            rating=request.json.get("rating"),
            author_id=request.json.get("author_id"),
            active=request.json.get("active")
        )
        db.session.add(comment)
    db.session.commit() 
    
    # successfully created comment, return recommended doctors
    doctors = Doctor.recommend_doctors()

    response = jsonify(doctors)
    response.status_code = 200

    return response


@flask_app.route("/comment/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    if not request.json:
        abort(400)

    # only update below fields
    rating = request.json.get("rating")
    comment_body = request.json.get("comment_body")
    active = request.json.get("active")

    comment = Comment.query.get(comment_id)
    
    if rating:
        comment.rating = rating
    if comment_body:
        comment.comment_body = comment_body
    if active is not None:
        comment.active = active

    db.session.commit()
    
    data = comment.format()

    response = jsonify(data)
    response.status_code = 200

    return response  


