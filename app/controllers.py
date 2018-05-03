from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

from app import flask_app
from models import db, Doctor, Comment

@flask_app.route('/comment/<int:comment_id>')
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)

    data = format_comment(comment)

    response = jsonify(data)
    response.status_code = 200

    return response


@flask_app.route('/comment', methods=['POST'])
def create_comment():
    if not request.json:
        abort(400)

    with db.session.begin(subtransactions=True):
        comment = Comment(
            doctor_id=request.json.get("doctor_id"),
            comment_body=request.json.get("comment_body"),
            rating=request.json.get("rating"),
            author_id=request.json.get("author_id"),
            archive=request.json.get("archive")
        )
        db.session.add(comment)
    db.session.commit() 
    
    data = format_comment(comment)

    response = jsonify(data)
    response.status_code = 200

    return response


@flask_app.route('/comment/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    if not request.json:
        abort(400)

    rating = request.json.get("rating")
    comment_body = request.json.get("comment_body")
    archive = request.json.get("archive")

    comment = Comment.query.get(comment_id)
    
    if rating:
        comment.rating = rating
    if comment_body:
        comment.comment_body = comment_body
    if archive:
        comment.archive = archive

    db.session.commit()
    
    data = format_comment(comment)

    response = jsonify(data)
    response.status_code = 200

    return response  


def format_comment(comment):
    return {
        "id": comment.id,
        "doctor_id": comment.doctor_id,
        "comment_body": comment.comment_body,
        "rating": comment.rating,
        "author_id": comment.author_id,
        "archive": comment.archive,
        "created_at": comment.created_at,
        "updated_at": comment.updated_at
    }
    