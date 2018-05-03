from datetime import datetime

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Boolean, 
    Column, 
    DateTime, 
    DECIMAL, 
    Integer, 
    JSON, 
    String, 
    Text,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database

from app import flask_app

if not database_exists(flask_app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(flask_app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(flask_app)

migrate = Migrate(flask_app, db)

doctors_specialties = db.Table('doctors_specialties',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctor.id'), primary_key=True),
    db.Column('specialty_id', db.Integer, db.ForeignKey('specialty.id'), primary_key=True)
)

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

class Specialty(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    doctors = db.relationship('Doctor', secondary=doctors_specialties, lazy='subquery',
        backref=db.backref('specialty', lazy=True))

class Comment(db.Model):
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer)
    comment_body = Column(Text)
    rating = Column(Integer)
    author_id = Column(Integer)
    archive = Column(Boolean)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
