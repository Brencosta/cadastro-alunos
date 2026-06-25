from models.aluno import Aluno

class AlunoRepository:

    def __init__(self, repository): # incializa o repositório de alunos
        self.repository = repository
    def cadastrar(self, aluno):
      if nome == "":
            raise Exception("nome obrigatoiiro")

      if idade < 0:
            raise Exception("idade inavlida")

      if "@" not in email:
            raise Exception("email invalido")
      aluno = Aluno(
           nome = nome,
           idade = idade,
           email = email
      )
      return self.repository.cadastrar(aluno)
   


  