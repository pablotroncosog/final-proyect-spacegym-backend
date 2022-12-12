import os    
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_cors import CORS   
from flask_bcrypt import Bcrypt 
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.utils import secure_filename
from models import db, User, Shopping, Order, Product, Category



BASEDIR = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__) #instancia de flask  
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASEDIR, "auth.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False     
app.config["ENV"] = "development"
app.config["SECRET_KEY"] = "super_secret_key"
app.config["JWT_SECRET_KEY"] = "super_jwt_key"
app.config["UPLOAD_FOLDER"] = os.path.join(BASEDIR, "images")#directorio de imagenes


CORS(app)
db.init_app(app)
Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return "Hello Flask"

@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        print(request.files)
        return jsonify({"msg": "No file in request"}) 
    file = request.files["file"] 
    if file.filename == "":
        return jsonify({"msg": "No file selected"})            
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return jsonify({"msg": "File saved"})      


@app.route("/users")
#@jwt_required()
def users():
    all_users = User.query.all()
    all_users = list(map(lambda user: user.serialize(), all_users))
    return jsonify({
        "data": all_users
    })


<<<<<<< HEAD

@app.route("/upload_image", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return "No file in request"
    file = request.files["file"]
    if file.filename == "":
        return "No file selected or file without name"
    if  file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return "File saved"



=======
>>>>>>> f83e2fc566562d992b6d8b33e89e2886a0465006
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

    found_user = user.query.filter_by(email=email).first()
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
        "data": found_user.serialize()
    }), 200


@app.route("/product", methods=["POST"])
def add_product():
    product = Product()
    product.name = request.json.get("name")
    product.price = request.json.get("price")
    product.description = request.json.get("description")
    product.category_id = request.json.get("category_id")
   

    db.session.add(product)
    db.session.commit()
    return "creado"


@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    all_products= list(map(lambda product: product.serialize(), products))
    return jsonify(all_products)

@app.route("/category", methods=["POST"])
def add_category():
    category = Category()
    category.name = request.json.get("name")
       
    db.session.add(category)
    db.session.commit()
    return "Categoria Creada"


@app.route("/category", methods=["GET"])
def get_category():
    category = Category.query.all()
    all_category = list(map(lambda category: category.serialize(), category))
    return jsonify(all_category)



if __name__ == "__main__":
    app.run(host="localhost", port=8080)