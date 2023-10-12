from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import get_key

from routers.routers import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

app.config["SQLALCHEMY_DATABASE_URI"] = get_key(".env", "SQLALCHEMY_DATABASE_URI")
print("Connecting to the database at:", app.config["SQLALCHEMY_DATABASE_URI"])
db = SQLAlchemy(model_class=DeclarativeBase)
db.init_app(app)

with app.app_context():
    db.create_all()
