# local onde fica os metodos do professor
from database import db
from models.professor import Professor 
class ProfessorRepository:
    def salvar(self, professor):
        db.session.add(professor)
        db.session.commit()
        return professor
    
    def deletar(self, professor):
        db.session.delete(professor)
        db.session.commit()

    def atualizarID(self, professor):
        db.session.commit()
        return professor  
    
    def listarall(self):
        return Professor.query.all()
    
    def buscarID(self, professorId):
        return Professor.query.get(professorId)