from flask_sqlalchemy import SQLAlchemy
from models import db, Doctor
from app import flask_app

# flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(flask_app)

@flask_app.route('/')
def hey_there():
	admin = Doctor(name='admin')
	db.session.begin(subtransactions=True)
	db.session.add(admin)
	db.session.commit()    
	return 'Oh hey there!'