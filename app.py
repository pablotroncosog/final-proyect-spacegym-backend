from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

app = Flask(__name__)

