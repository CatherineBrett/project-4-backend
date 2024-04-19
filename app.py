from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config.environment import db_URI


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

CORS(app)

db = SQLAlchemy(app)

marsh = Marshmallow(app)

bcrypt = Bcrypt(app)

from controllers import groups, users

app.register_blueprint(groups.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")
