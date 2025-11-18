from .swaggerinit import api

def configure_swagger(app):
    from .namespace.usuarionamespace import api as usuarios_ns
    from .namespace.agendanamespace import api as agenda_ns

    api.init_app(app)

    api.add_namespace(usuarios_ns, path="/usuarios")
    api.add_namespace(agenda_ns, path="/agenda") 

    api.mask_swagger = False