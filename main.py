from flask import Flask, request, jsonify
from models.aluno import Aluno
from models.curso import Curso
from models.professor import Professor
from models.matricula import Matricula

from database import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///escola.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)



@app.route("/alunos", methods=["POST"])
def cadastrar_aluno():

    dados = request.get_json()

    aluno = Aluno(
        nome=dados["nome"],
        email=dados["email"],
        matricula=dados["matricula"]
    )

    db.session.add(aluno)
    db.session.commit()

    return jsonify({
        "message": "Aluno cadastrado",
        "id": aluno.id
    }), 201



@app.route("/alunos/<int:id>", methods=["GET"])
def buscar_aluno(id):

    aluno = Aluno.query.get(id)

    if aluno is None:
        return jsonify({"error": "Aluno não encontrado"}), 404

    return jsonify({
        "id": aluno.id,
        "nome": aluno.nome,
        "email": aluno.email,
        "matricula": aluno.matricula
    })



@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):

    dados = request.get_json()

    aluno = Aluno.query.get(id)

    if aluno is None:
        return jsonify({"error": "Aluno não encontrado"}), 404


    aluno.nome = dados.get("nome")
    aluno.email = dados.get("email")
    aluno.matricula = dados.get("matricula")

    db.session.commit()

    return jsonify({
        "message": "Aluno atualizado"
    })



@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):

    aluno = Aluno.query.get(id)

    if aluno is None:
        return jsonify({"error": "Aluno não encontrado"}), 404


    db.session.delete(aluno)
    db.session.commit()

    return jsonify({
        "message": "Aluno removido"
    })



@app.route("/cursos", methods=["POST"])
def cadastrar_curso():

    dados = request.get_json()

    curso = Curso(
        nome=dados["nome"]
    )

    db.session.add(curso)
    db.session.commit()

    return jsonify({
        "message": "Curso cadastrado",
        "id": curso.id
    }), 201



@app.route("/cursos/<int:id>", methods=["GET"])
def buscar_curso(id):

    curso = Curso.query.get(id)

    if curso is None:
        return jsonify({"error": "Curso não encontrado"}),404


    return jsonify({
        "id": curso.id,
        "nome": curso.nome
    })


@app.route("/professores", methods=["POST"])
def cadastrar_professor():

    dados = request.get_json()

    professor = Professor(
        nome=dados["nome"],
        email=dados["email"]
    )

    db.session.add(professor)
    db.session.commit()


    return jsonify({
        "message":"Professor cadastrado",
        "id": professor.id
    }),201



@app.route("/professores/<int:id>", methods=["GET"])
def buscar_professor(id):

    professor = Professor.query.get(id)

    if professor is None:
        return jsonify({"error":"Professor não encontrado"}),404


    return jsonify({
        "id": professor.id,
        "nome": professor.nome,
        "email": professor.email
    })


@app.route("/matriculas", methods=["POST"])
def cadastrar_matricula():

    dados = request.get_json()


    matricula = Matricula(
        aluno_id=dados["aluno_id"],
        curso_id=dados["curso_id"]
    )


    db.session.add(matricula)
    db.session.commit()


    return jsonify({
        "message":"Matrícula realizada",
        "id":matricula.id
    }),201



@app.route("/matriculas/<int:id>", methods=["GET"])
def buscar_matricula(id):

    matricula = Matricula.query.get(id)

    if matricula is None:
        return jsonify({"error":"Matrícula não encontrada"}),404


    return jsonify({
        "id":matricula.id,
        "aluno_id":matricula.aluno_id,
        "curso_id":matricula.curso_id
    })



@app.route("/matriculas/<int:id>", methods=["DELETE"])
def deletar_matricula(id):

    matricula = Matricula.query.get(id)

    if matricula is None:
        return jsonify({"error":"Matrícula não encontrada"}),404


    db.session.delete(matricula)
    db.session.commit()


    return jsonify({
        "message":"Matrícula removida"
    })



# Criar tabelas
with app.app_context():
    db.create_all()



if __name__ == "__main__":
    app.run(debug=True)