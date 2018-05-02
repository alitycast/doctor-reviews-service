from app import flask_app
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy(flask_app, session_options={
    'autocommit': True,
    'autoflush': False,
    'expire_on_commit': False
})

migrate = Migrate(flask_app, db)

class Doctor(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
