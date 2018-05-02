from flask import Flask

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

import controllers