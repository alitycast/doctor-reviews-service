from flask_sqlalchemy import SQLAlchemy
from models import db, Doctor
from app import flask_app

@flask_app.route('/')
def hey_there():
	with db.session.begin(subtransactions=True):
		admin = Doctor(name='ali')
		db.session.add(admin)
	db.session.commit() 
	return 'Oh hey there!'