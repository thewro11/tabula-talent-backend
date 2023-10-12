from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import get_key

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = get_key(".env", "SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

from controllers import *
