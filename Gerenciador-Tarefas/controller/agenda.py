from flask import *
import flask 
from models import agenda

url2 = flask.Blueprint("app_pb2", __name__)

        
@url2.route("/task",methods=["GET"])
def get_tasks():
        response = agenda.listaAgenda()
        return response


@url2.route("/task",methods=["GET"], strict_slashes=False)
def get_task():
        data = request.get_json() 
        task_id = data.get("task_id")
        return atualizaAgenda(task_id)


@url2.route("/task",methods=["POST"], strict_slashes=False)
def post_task():
        data = request.get_json()
        response = agenda.insereAgenda(data.get('titulo'), data.get('descricao'), data.get('id_usuario'), data.get('prazo_final'))

        return response

@url2.route("/task", methods=["PUT"], strict_slashes=False)
def update_task():
        data = request.get_json()  
        task_id = data.get('id') 
        response = atualizaTarefa(id)
        
        return response
        
@url2.route("/task",methods=["DELETE"])
def delete_task():
        task_id = flask.request.args.get("task_id")
        response = agenda.deletaTarefaSQL(task_id)
        return response
        