from database import db

class Matricula(db.Model):
    __tablename__ = "matriculas"

    id = db.Column(db.Integer, primary_key=True)
# criando relacionamento entre aluno e curso
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id"))
    curso_id = db.Column(db.Integer, db.ForeignKey("cursos.id"))