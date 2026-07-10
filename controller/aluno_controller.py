from flask import request, jsonify

class AlunoController:
    def __init__(self, Aluno_service):
        self.Aluno_service = Aluno_service
    def cadastrar(self):
        dados = request.get_json()

        email = dados.get('email')
        nome = dados.get('nome')
        matricula = dados.get('matricula')
        try:
            aluno = self.Aluno_service.cadastrar(id, email, nome, matricula)
            return jsonify({'message': 'Aluno cadastrado com sucesso'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    def deletar(self, aluno_id):
        try:
            aluno = self.Aluno_service.buscar_por_id(aluno_id)
            self.Aluno_service.deletar(aluno)
            return jsonify({'message': 'Aluno deletado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    def buscar_por_id(self, aluno_id):
        try:
            aluno = self.Aluno_service.buscar_por_id(aluno_id)
            if aluno is None:
                return jsonify({'error': 'Aluno não encontrado'}), 404
            return jsonify({
                'id': aluno.id,
                'email': aluno.email,
                'nome': aluno.nome,
                'matricula': aluno.matricula
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    def buscar(self):
        try:
            alunos = self.Aluno_service.buscar()
            if not alunos:
                return jsonify({'error': 'Nenhum aluno encontrado'}), 404
            alunos_data = []
            for aluno in alunos:
                alunos_data.append({
                    'id': aluno.id,
                    'email': aluno.email,
                    'nome': aluno.nome,
                    'matricula': aluno.matricula
                })
            return jsonify(alunos_data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
def atualizar(self, aluno_id):
    dados = request.get_json()

    try:
        aluno = self.Aluno_service.buscar_por_id(aluno_id)

        if aluno is None:
            return jsonify({"error": "Aluno não encontrado"}), 404

        aluno.nome = dados.get("nome")
        aluno.email = dados.get("email")
        aluno.matricula = dados.get("matricula")

        self.Aluno_service.atualizar(aluno)

        return jsonify({"message": "Aluno atualizado com sucesso"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400