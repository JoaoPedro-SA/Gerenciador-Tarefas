from flask import jsonify, request
import models.bancoSQL as banco

def geradorDeId(dados):
    if len(dados["usuarios"]) == 0:
        return 1
    else:
        return dados["usuarios"][-1]["id"] + 1


def listaUsuario(): 
    response = []
    try: 
        usuario = banco.session.query(banco.usuario).all()
        for u in usuario: 
            response.append({"id": u.id, "nome": u.name, "email": u.email})
    except Exception as e:
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)
        
def pegaUsuario(idBuscado):
    usuario = banco.session.query(banco.usuario).filter_by(id=idBuscado).first()
    try:
        if usuario.id == idBuscado:
            response = {"id": usuario.id, "nome": usuario.name, "email": usuario.email}
    except Exception as e: 
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def insereUsuario(name,email):
    novo_usuario = banco.usuario(name=name, email=email)
    try:
        banco.session.add(novo_usuario)
        banco.session.commit()
        response = {"id": novo_usuario.id, "nome": novo_usuario.name, "email": novo_usuario.email}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def atualizarUsuario(id,name,email):
    try:
        usuario = banco.session.query(banco.usuario).filter_by(id=id).first()
        if usuario:
            usuario.name = name
            usuario.email = email
            banco.session.commit()
            response = {"id": usuario.id, "nome": usuario.name, "email": usuario.email}
        else:
            response = {"message": "Usuário não encontrado"}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def deletarUsuario(id):
    try: 
        status = banco.session.query(banco.usuario).filter_by(id=id).delete()
        banco.session.commit()
        if status:
            response = {"message": "Usuário deletado com sucesso"}
        else:
            response = {"message": "Usuário não encontrado"}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)    