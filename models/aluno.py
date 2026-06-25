from database import db
class Aluno(db.Model):
    id = db.column(db.Integer, primary_key=True)
    nome = db.column(db.String(100), nullable=False)
    email = db.column(db.String(100), unique=True, nullable=False) 
    matricula = db.column(db.String(20), unique=True, nullable=False)
