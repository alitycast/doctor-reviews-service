from flask import Flask

flask_app = Flask(__name__)
flask_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/doctor"

import controllers