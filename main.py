from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from models import aluno
app = Flask (__name__)
# craido o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():  # ta criando a tabela no banco de dados, tem que ser dentro do app_context para ter acesso ao banco
    db.create_all()

@app.route("/cadastrar", methods =["POST"])
def cadastrar():
    nome = request.form.get("nome")
    idade = request.form.get("idade")
    aluno_novo = aluno(nome=nome, idade=idade)
    db.session.add(aluno_novo)
    db.session.commit()
    return "Aluno cadastrado com sucesso!"







app.run()