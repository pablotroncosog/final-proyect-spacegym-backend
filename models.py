from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() #instancia de SQALchemy

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    shopping = db.relationship("Shopping")


    def __repr__(self):
        return"<User %r>" % self.name

    def serialize (self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
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
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id") )
    category = db.relationship("Category")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category": {
                "id":self.category.id,
                "name":self.category.name
            }
        }

class Category (db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    


