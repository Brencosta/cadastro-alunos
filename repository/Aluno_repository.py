from models.aluno import Aluno

def salvar(self, aluno):
        db.session.add(aluno)
        db.session.commit()
        return aluno

def buscar_por_id(self, aluno_id):
        return Aluno.query.get(aluno_id)
