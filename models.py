from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # instancia de SQALchemy


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


class Shopping(db.Model):
    __tablename__ = "shoppings"
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User")

    def serialize(self):
        return {
            "id": self.id,
            "order": self.order,
            "price": self.price,
            "date": self.date,
            "status": self.status,
            "user": {self.user.id
                     }
        }


class Sale(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User")


user = db.relationship("User")


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category")
    category = db.relationship("Category")
    user = db.relationship("User")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "description": self.description,
            "id": self.category.id,
            "name": self.category.name,
            "user": {self.user.id
                     }
        }


class Category (db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            "category": {
                "id": self.id,
                "name": self.name
            }
        }
