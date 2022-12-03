from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() #instancia de SQALchemy

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50) )
    province = db.Column(db.String(50))
    street = db.Column(db.String(50) )
    birthday = db.Column(db.Date)
    gender = db.Column(db.String(50))
    role = db.Column(db.Boolean)


    def __repr__(self):
        return"<User %r>" % self.name

    def serialize (self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # "password": self.password
           
        }


class Shopping(db.Model):
    __tablename__ = "shoppings"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }


class Category (db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    gym = db.Column(db.Boolean, nullable=False)
    combat = db.Column(db.Boolean, nullable=False)
    yoga = db.Column(db.Boolean, nullable=False)
    genera_sport = db.Column(db.Boolean, nullable=False)
