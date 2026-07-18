from flask import request, jsonify

class ProfessorController:
    def __init__(self, Matricula_service):
        self.Matricula_service = Matricula_service

    def cadastrar(self):
        dados = request.get_json()
        aluno_id = dados.get('aluno_id')
        curso_id = dados.get('curso_id')
        try:
            matricula = self.Matricula_service.salvar(aluno_id, curso_id)
            return jsonify({'mensagem': 'Matrícula cadastrada com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def deletar(self, matricula_id):
        try:
            matricula = self.Matricula_service.buscar_por_id(matricula_id)
            if matricula is None:
                return jsonify({"error": "Matrícula não encontrada"}), 404
            self.Matricula_service.deletar(matricula)
            return jsonify({"mensagem": "Matrícula deletada com sucesso"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def buscar_por_id(self, matricula_id):
        try:
            matricula = self.Matricula_service.buscar_por_id(matricula_id)
            if matricula is None:
                return jsonify({"error": "Matrícula não encontrada"}), 404
            return jsonify(matricula.to_dict()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
