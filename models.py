#entidades
from sqlalchemy import false, true
from main import db

class aluno(db.Model): # cria a classe(modelo) aluno, que está heradndo db.model sinalziando que é uma tabela do banco.
    id = db.Column(db.Integer, primary_key=True) # estamos criando uma coluna no banco, do tipo inteiro e ela é a chave primaria
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    matricula = db.Column(db.Integer, nullable=False)
