from flask import *
import flask 
from models.agenda import *

url2 = flask.Blueprint("app_pb2", __name__)

        
@url2.route("/task",methods=["GET"])
def get_tasks():
        response = listaAgenda()
        return response


@url2.route("/task",methods=["PUT"], strict_slashes=False)
def get_task():
        data = request.get_json() 
        task_id = data.get("task_id")
        return atualizarAgenda(task_id, data)


@url2.route("/task",methods=["POST"], strict_slashes=False)
def post_task():
        data = request.get_json()
        response = insereAgenda(data.get('titulo'), data.get('descricao'), data.get('id_usuario'), data.get('prazo_final'))

        return response
        
@url2.route("/task/<int:task_id>", methods=["PUT", "OPTIONS"])
def update_task(task_id):
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json()
    return atualizarAgenda(task_id, data)

        
@url2.route("/task/<int:task_id>", methods=["DELETE", "OPTIONS"], strict_slashes=False)
def delete_task(task_id):
    if request.method == "OPTIONS":
        return "", 200

    return deletarAgenda(task_id)
