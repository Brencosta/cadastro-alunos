from flask import request, jsonify

class CursoController:
    def __init__(self, Curso_service):
        self.Curso_service = Curso_service
    def cadastrar(self):
        dados = request.get_json()
        nome = dados.get('nome')
        descricao = dados.get('descricao')
        try:
            curso = self.Curso_service.salvar(nome, descricao)
            return jsonify({'messagem': 'Crso cadastrado com sucesso'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    def deletar(self, curso_id):
        try:
            curso = self.Curso_service.buscar_por_id(curso_id)
            self.Curso_service.deletar(curso)
            return jsonify({"mensagem: Curso deletado com sucesso"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    def atualizar(self, curso_id):
        dados  = request.get_json()
        try:
            curso = self.Curso_service.buscar_por_id(curso_id)
            if curso is None:
                return jsonify({"error": "Curso não encontrado"}), 404
            nome = dados.get('nome')
            descricao = dados.get('descricao')
            self.Curso_service.atualizar(curso, nome, descricao)
            return jsonify({"mensagem": "Curso atualizado com sucesso"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    def buscar_por_id(self, curso_id):
        try:
            curso = self.Curso_service.buscar_por_id(curso_id)
            if curso is None:
                return jsonify({"error": "Curso não encontrado"}), 404
            return jsonify(curso.to_dict()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400