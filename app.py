from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.environment import db_URI

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"


app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

db = SQLAlchemy(app)
