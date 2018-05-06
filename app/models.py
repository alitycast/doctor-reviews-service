from datetime import datetime

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    DECIMAL, 
    inspect,
    Integer, 
    JSON, 
    String, 
    Text,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database

from app import flask_app

# Database setup
if not database_exists(flask_app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(flask_app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

# Tables 
doctors_specialties = db.Table('doctors_specialties',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctor.id'), primary_key=True),
    db.Column('specialty_id', db.Integer, db.ForeignKey('specialty.id'), primary_key=True)
)

# Models 
class Doctor(db.Model):
    id = Column(Integer, primary_key=True)
    group_id = Column(String(255), index=True)
    name = Column(String(255))
    address = Column(JSON)
    latitude = Column(DECIMAL(10, 8))
    longitude = Column(DECIMAL(11, 8)) 
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    specialties = db.relationship('Specialty', secondary=doctors_specialties, lazy='subquery',
        backref=db.backref('doctor', lazy=True))

    @classmethod
    def recommend_doctors(cls):
        query_result = Comment.query.filter_by(rating=5).limit(5)

        doctor_ids = [result.doctor_id for result in query_result]

        doctors = [Doctor.query.get(doctor_id).__dict__ for doctor_id in doctor_ids]

        # removes unnecessary field which isn't JSON serializable
        [doctor.pop('_sa_instance_state', None) for doctor in doctors]

        return doctors

class Specialty(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    doctors = db.relationship('Doctor', secondary=doctors_specialties, lazy='subquery',
        backref=db.backref('specialty', lazy=True))

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, index=True)
    comment_body = Column(Text)
    rating = Column(Integer)
    author_id = Column(Integer, index=True)
    active = Column(Boolean, index=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def format(self):
        return {
            "id": self.id,
            "doctor_id": self.doctor_id,
            "comment_body": self.comment_body,
            "rating": self.rating,
            "author_id": self.author_id,
            "active": self.active,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }