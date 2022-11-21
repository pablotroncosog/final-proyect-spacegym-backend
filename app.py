from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Shopping, Order, Product, Category

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(BASEDIR, "spacegym.db")

db.init_app(app)
Migrate(app, db)
CORS(app)


@app.route("/product", methods=["POST"])
def add_product():
    product = Product()
    product.name = request.json.get("name")
    product.price = request.json.get("price")
    product.description = request.json.get("description")

    db.session.add(product)
    db.session.commit()
    return "creado"


@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    all_products= list(map(lambda product: product.serialize(), products))
    return jsonify(all_products)
    


if __name__ == "__main__":
    app.run(host="localhost", port=8081)
