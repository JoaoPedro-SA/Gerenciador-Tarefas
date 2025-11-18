from flask_restx import Namespace, Resource, fields
from models import agenda as model

api = Namespace('agenda', description='Operações com tarefas')

agenda_model = api.model('Tarefa', {
    'id': fields.Integer(readonly=True, description='ID da tarefa'),
    'titulo': fields.String(required=True, description='Título da tarefa'),
    'descricao': fields.String(required=True, description='Descrição da tarefa'),
    'id_usuario': fields.Integer(required=True, description='ID do usuário'),
    'prazo_final': fields.String(required=True, description='Prazo final da tarefa (YYYY-MM-DD)')
})

@api.route('/')
class TaskList(Resource):
    @api.marshal_list_with(agenda_model)
    def get(self):
        """Lista todas as tarefas"""
        return model.listaAgenda().json

    @api.expect(agenda_model)
    @api.marshal_with(agenda_model, code=201)
    def post(self):
        """Cria uma nova tarefa"""
        data = api.payload
        return model.insereAgenda(data['titulo'], data['descricao'], data['id_usuario'], data['prazo_final']).json, 201

@api.route('/<int:id>')
@api.response(404, 'Tarefa não encontrada')
class Task(Resource):
    @api.marshal_with(agenda_model)
    def get(self, id):
        """Busca uma tarefa pelo ID"""
        return model.pegaAgenda(id).json

    @api.expect(agenda_model)
    @api.marshal_with(agenda_model)
    def put(self, id):
        """Atualiza uma tarefa"""
        data = api.payload
        return model.atualizaTarefa(id, data['titulo'])