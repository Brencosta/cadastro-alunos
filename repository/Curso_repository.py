from database import db
from models.curso import Curso

class CursoRepository:

    def salvar(self, curso):
        db.session.add(curso)
        db.session.commit()
        return curso
    def buscar_por_id(self, curso_id):
        return Curso.query.get(curso_id)
    
    def deletar(self, curso):
        db.session.delete(curso)
        db.session.commit()

    def atualizar(self, curso):
        db.session.commit()
        return curso
  