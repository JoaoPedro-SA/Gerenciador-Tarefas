from flask import *
import flask
from models import usuario

url = flask.Blueprint("app_pb", __name__)

@url.route("/user",methods=["GET"])
def get_users():
        response = usuario.listaUsuario()
        return response

@url.route("/user/<int:id>",methods=["GET"])
def get_user(id):
        response = usuario.pegaUsuario(id)
        return response


@url.route("/user",methods=["POST"], strict_slashes=False)
def post_user():
        data = request.get_json()
        response = usuario.insereUsuario(data.get('nome'), data.get('email'))
        return response

@url.route("/user", methods=["PUT"], strict_slashes=False)
def update_user():
    nome = flask.request.args.get("nome")
    email = flask.request.args.get("email")
    user_id = flask.request.args.get("user_id")
    response = usuario.atualizarUsuario(user_id, nome, email)
    return response
        
@url.route("/user",methods=["DELETE"], strict_slashes=False)
def delete_user():
        user_id = flask.request.args.get("user_id")
        response = usuario.deletarUsuario(user_id)
        return response
        