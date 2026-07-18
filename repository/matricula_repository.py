from database import db
from models.aluno import Aluno

class matriculaRepository:

    def salvar(self, matricula):
        db.session.add(matricula)
        db.session.commit()
        return matricula

    def buscar_por_id(self, matricula_id):
        return Aluno.query.get(matricula_id)
    
    def deletar(self, matricula):
        db.session.delete(matricula)
        db.session.commit()

    def atualizar(self, matricula):
        db.session.commit()
        return matricula