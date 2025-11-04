from flask_restx import Namespace, Resource, fields
from models import usuario as model

api = Namespace('usuarios', description='Operações com usuários')

usuario_model = api.model('Usuario', {
    'id': fields.Integer(readonly=True, description='ID do usuário'),
    'nome': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário')
})

@api.route('/')
class UsuarioList(Resource):
    @api.marshal_list_with(usuario_model)
    def get(self):
        """Lista todos os usuários"""
        return model.listaUsuario().json

    @api.expect(usuario_model)
    @api.marshal_with(usuario_model, code=201)
    def post(self):
        """Cria um novo usuário"""
        data = api.payload
        return model.insereUsuario(data['nome'], data['email']).json, 201

@api.route('/<int:id>')
@api.response(404, 'Usuário não encontrado')
class Usuario(Resource):
    @api.marshal_with(usuario_model)
    def get(self, id):
        """Busca um usuário pelo ID"""
        return model.pegaUsuario(id).json

    @api.expect(usuario_model)
    @api.marshal_with(usuario_model)
    def put(self, id):
        """Atualiza usuário"""
        data = api.payload
        return model.atualizarUsuario(id, data['nome'], data['email']).json

    @api.response(204, 'Usuário deletado')
    def delete(self, id):
        """Deleta usuário"""
        return model.deletarUsuario(id).json, 204
