from flask import *
import flask
from models import usuario

url = flask.Blueprint("app_pb", __name__)

@url.route("/users",methods=["GET"])
def get_users():
        response = usuario.listaUsuario()
        return response

@url.route("/user/<int:id>",methods=["GET"])
def get_user(id):
        response = usuario.pegaUsuario(id)
        return response


@url.route("/user",methods=["POST"], strict_slashes=False)
def post_user():
        name = flask.request.args.get("nome")
        email = flask.request.args.get("email")
        response = usuario.insereUsuario(name, email)
        return response

@url.route("/users", methods=["PUT"], strict_slashes=False)
def update_user():
    name = flask.request.args.get("nome")
    email = flask.request.args.get("email")
    user_id = flask.request.args.get("user_id")
    response = usuario.atualizarUsuario(user_id, name, email)
    return response
        
@url.route("/users",methods=["DELETE"], strict_slashes=False)
def delete_user():
        user_id = flask.request.args.get("user_id")
        response = usuario.deletarUsuario(user_id)
        return response
        