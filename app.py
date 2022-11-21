import os    
from flask import Flask, jsonify, request   
from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate 
from flask_cors import CORS   
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import db, User

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__) #instancia de flask  
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
     os.path.join(BASEDIR, "auth.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False     
app.config["ENV"] = "development"
app.config["SECRET_KEY"] = "super_secret_key"
app.config["JWT_SECRET_KEY"] = "super_jwt_key"

CORS(app)
db.init_app(app)
Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@app.route("/")
def home():
    return "Hello Flask"

@app.route("/users")
#@jwt_required()
def users():
    all_users = User.query.all()
    all_users = list(map(lambda user: user.serialize(), all_users))
    return jsonify({
        "data": all_users
    })

@app.route("/login", methods=["POST"])
def login():
    password = request.json.get("password")
    email = request.json.get("email")

    found_user = User.query.filter_by(email=email).first()

    if found_user is None:
        return jsonify({
            "msg":"user not found please create user"
        }), 404
        
    if bcrypt.check_password_hash(found_user.password, password):
        access_token = create_access_token(identity=email)
        return jsonify({
            "access_token": access_token,
            "data": found_user.serialize(),
            "success": True
        }), 200 
    else:
        return jsonify({
            "msg": "password is invalid"
        })        


@app.route("/user", methods=["POST"])
def user():
    user = User()
    password = request.json.get("password")
    email = request.json.get("email")
    name = request.json.get("name")

    found_user = User.query.filter_by(email=email).first()
    print(found_user)
    if found_user is not None:
        return jsonify({
            "msg":"Email is already in use"
        }), 400
    
    user.email = email
    user.name = name
    password_hash = bcrypt.generate_password_hash(
        password) #encriptando la contraseña con bcrypt
    user.password = password_hash    
    
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "msg": "success creating user", 
        "data": user.serialize()
    }), 200


if __name__ == "__main__":
    app.run(port=8080, host="localhost")