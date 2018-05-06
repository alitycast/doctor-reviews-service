from app.app import flask_app
from app.models import Comment, db, Doctor


def test_recommend_doctors():
    with db.session.begin(subtransactions=True):
        doctor = Doctor()
        db.session.add(doctor)

    doc = Doctor.query.first()

    with db.session.begin(subtransactions=True):
        comment = Comment(doctor_id=doc.id, rating=5)
        db.session.add(comment)

    doctors = Doctor.recommend_doctors()

    assert isinstance(doctors, list)
    assert len(doctors) == 1