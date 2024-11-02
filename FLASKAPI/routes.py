from flask import Blueprint, jsonify, request
from models import db, Book,User
from collections import OrderedDict
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
api = Blueprint('api', __name__)

@api.route("/books",methods=["GET"])
def get_books():
    books=Book.query.order_by(Book.id).all()
    book_list=[
        {
           "id":book.id,
           "title":book.title,
           "author":book.author,
           "description":book.description
        }
        for book in books
    ]
    return jsonify(book_list)

@api.route("/add",methods=["POST"])
@jwt_required()
def add():
    data=request.get_json()
    new_book=Book(title=data["title"],author=data["author"],description=data["description"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"state":"success"}),201

@api.route("/book/<int:id>",methods=["GET"])

def book(id):
    book=Book.query.get(id)
    return jsonify({
      "id":book.id,
      "title":book.title,
      "author":book.author,
      "description":book.description

    }),200

@api.route("/delete/<int:id>",methods=["DELETE"])
@jwt_required()
def delete(id):
    book=Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({
      "state":"success delete"

    })

@api.route("/update/<int:id>",methods=["PUT"])
@jwt_required()
def update(id):
    book=Book.query.get(id)
    newbook=request.get_json()
    book.title=newbook.get("title",book.title)
    book.author=newbook.get("author",book.author)
    book.description=newbook.get("description",book.description)
    db.session.commit()
    return jsonify({
        "state":"update success"
    })

@api.route("/signup",methods=["Post"])
def signup():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")

    existing_user=User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message":"Username already exists"}),400
    
    new_user=User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201

@api.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"msg": "Invalid username or password"}), 401
    
    access_token= create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
    


    











    
    

     

    

