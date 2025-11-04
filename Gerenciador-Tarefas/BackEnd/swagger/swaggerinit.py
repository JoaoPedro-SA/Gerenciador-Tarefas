from flask_restx import Api

api = Api(
    title="API de Tarefas", 
    version="1.0",
    description="Gerenciador de Tarefas",
    doc="/docs",
    prefix="/api",
)