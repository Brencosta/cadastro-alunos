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
    dados = request.get_json()

    aluno = Aluno(  # criando objetoi do tipo aluno 
        nome=dados["nome"],
        email=dados["email"],
        matricula=dados["matricula"]
    )

    db.session.add(aluno)
    db.session.commit()

    return {
        "mensagem": "Aluno cadastrado com sucesso!"
    }, 201
    
@app.route("/alunoos", methods =["GET"])
def listar_alunos():
    alunos = Aluno.query.all() # consulta todos os alunos do banco de dados
    resultado = []
    for aluno in alunos:
        resultado.append({ # addciono mna lista vazia formando um dicionartio
            "id": aluno.id,
            "nome": aluno.nome,
            "email": aluno.email,
            "matricula": aluno.matricula
        })
    return {
        "alunos": resultado
    }, 200

@app.route("/deletar/<int:id>", methods =["DELETE"])
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return {
            "mensagem": "Aluno não encontrado!"
        }, 404

    db.session.delete(aluno)
    db.session.commit()

    return {
        "mensagem": "Aluno deletado com sucesso!"
    }, 200

app.run()