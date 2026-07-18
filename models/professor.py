from database import db
class Professor(db.Model):
    __tablename__ = "professores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False) 
    disciplina = db.Column(db.String(50), nullable=False)
  # craiando relacionamento entre professor e curso
    cursos = db.relationship("Curso", backref="professor")