from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() #instancia de SQALchemy

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return"<User %r>" % self.name

    def serialize (self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }