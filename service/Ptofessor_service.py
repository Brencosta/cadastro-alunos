from models.professor import Professor


class ProfessorService:

    def __init__(self, repository):
        self.repository = repository

    def salvar(self, nome, email, disciplina):

        if nome == "":
            raise Exception("Nome obrigatório")

        if "@" not in email:
            raise Exception("Email inválido")

        if disciplina == "":
            raise Exception("Disciplina obrigatória")

        professor = Professor(
            nome=nome,
            email=email,
            disciplina=disciplina
        )

        return self.repository.salvar(professor)

    def buscar_por_id(self, professor_id):

        if professor_id <= 0:
            raise Exception("ID inválido")

        return self.repository.buscar_por_id(professor_id)

    def buscar_todos(self):
        return self.repository.buscar_todos()

    def atualizar(self, professor):
        return self.repository.atualizar(professor)

    def deletar(self, professor):

        if professor is None:
            raise Exception("Professor não encontrado")

        return self.repository.deletar(professor)
    
    nome = "sdfghjk"