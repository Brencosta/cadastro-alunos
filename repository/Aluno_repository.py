from database import db
from models.aluno import Aluno


class AlunoRepository:

    def cadastrar(self, aluno):
        db.session.add(aluno)
        db.session.commit()
        return aluno

    def buscar_por_id(self, aluno_id):
        return Aluno.query.get(aluno_id)

    def buscar_todos(self):
        return Aluno.query.all()

    def deletar(self, aluno):
        db.session.delete(aluno)
        db.session.commit()

    def atualizar(self, aluno):
        db.session.commit()
        return aluno