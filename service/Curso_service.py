from models.curso import Curso
from repository.Curso_repository import CursoRepository
class CursoService:

    def __init__(self, repository):
        self.repository = repository

    def salvar(self, nome, descricao):

        if nome == "":
            raise Exception("Nome obrigatório")

        if descricao == "":
            raise Exception("Descrição obrigatória")

        curso = Curso(
            nome=nome,
            descricao=descricao
        )

        return self.repository.salvar(curso)

    def buscar_por_id(self, curso_id):

        if curso_id <= 0:
            raise Exception("ID inválido")

        return self.repository.buscar_por_id(curso_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()

    def atualizar(self, curso):
        return self.repository.atualizar(curso)

    def deletar(self, curso):

        if curso is None:
            raise Exception("Curso não encontrado")

        return self.repository.deletar(curso)