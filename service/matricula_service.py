from models.matricula import Matricula
from repository.matricula_repository import matriculaRepository
class MatriculaService:
    def __init__(self, repository):
        self.repository = repository
    def salvar(self, aluno_id, curso_id):
        if aluno_id <= 0:
            raise Exception("ID do aluno inválido")
        if curso_id <= 0:
            raise Exception("ID do curso inválido")
        matricula = Matricula(
            aluno_id=aluno_id,
            curso_id=curso_id
        )
        return self.repository.salvar(matricula)
    def buscar_por_id(self, matricula_id):
        if matricula_id <= 0:
            raise Exception("ID inválido")
        return self.repository.buscar_por_id(matricula_id) 
    def deletar(self, matricula):
        if matricula is None:
            raise Exception("Matrícula não encontrada")
        return self.repository.deletar(matricula)
    def atualizar(self, matricula):
        return self.repository.atualizar(matricula) 
    def buscar_todos(self):
        return self.repository.buscar_todos()   
    def desativar_matricula(self, matricula):
        if matricula is None:
            raise Exception("Matrícula não encontrada")
        matricula.ativa = False
        return self.repository.atualizar(matricula) 