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

@url.route("/user/<int:user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    data = flask.request.get_json()

    nome = data.get("nome")
    email = data.get("email")

    response = usuario.atualizarUsuario(user_id, nome, email)
    return response

        
@url.route("/user/<int:user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    response = usuario.deletarUsuario(user_id)
    return response
