from flask import jsonify, request
import models.bancoSQL as banco


def listaAgenda(): 
    response = []
    try: 
        agenda= banco.session.query(banco.agenda).all()
        for u in agenda: 
            response.append({"id": u.id, "descricao": u.descricao, "titulo": u.titulo, "id_usuario": u.id_usuario, "prazo_final": u.prazo_final})
    except Exception as e:
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)
        
def pegaAgenda(idBuscado):
    agenda = banco.session.query(banco.agenda).filter_by(id=idBuscado).first()
    try:
        if agenda.id == idBuscado:
            response = ({"id": agenda.id, "descricao": agenda.descricao, "titulo": agenda.titulo, "id_usuario": agenda.id_usuario, "prazo_final": agenda.prazo_final})
    except Exception as e: 
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def insereAgenda(descricao, titulo, id_usuario, prazo_final):
    nova_agenda = banco.agenda(descricao=descricao, titulo=titulo, id_usuario=id_usuario, prazo_final=prazo_final) 
    try:
        banco.session.add(nova_agenda)
        banco.session.commit()
        response = {"id": nova_agenda.id, "descricao": nova_agenda.descricao, "titulo": nova_agenda.titulo, "titulo": nova_agenda.titulo, "id_usuario": nova_agenda.id_usuario, "prazo_final": nova_agenda.prazo_final}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)

def atualizarAgenda(id, descricao, titulo, id_usuario, prazo_final):
    try:
        agenda = banco.session.query(banco.agenda).filter_by(id=id).first()
        if agenda:
            agenda.name = descricao
            agenda.descricao = descricao
            agenda.titulo = titulo
            agenda.id_usuario = id_usuario
            agenda.prazo_final = prazo_final
            banco.session.commit()
            response = {"id": agenda.id, "descricao": agenda.descricao, "titulo": agenda.titulo, "titulo": agenda.titulo, "id_usuario": agenda.id_usuario, "prazo_final": agenda.prazo_final}
        else:
            response = {"message": "Agenda não encontrada"}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)
         
def deletarAgenda(id):
    try: 
        status = banco.session.query(banco.agenda).filter_by(id=id).delete()
        banco.session.commit()
        if status:
            response = {"message": "Agenda deletada com sucesso"}
        else:
            response = {"message": "Agenda não encontrada"}
    except Exception as e:
        banco.session.rollback()
        response = {"erro": str(e)}
    finally:
        banco.session.close()
    return jsonify(response)    