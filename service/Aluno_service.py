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
    
    def buscar_por_id(self, aluno_id):
        if aluno_id <= 0:
            raise Exception("ID inválido")
        return self.repository.buscar_por_id(aluno_id)
    
    def buscar(self):
        if not self.repository.buscar():
            raise Exception("Nenhum aluno encontrado")
        return self.repository.buscar()
    
    def deletar(self, aluno): 
        if aluno is None:
            raise Exception("Aluno não encontrado")  
        return self.repository.deletar(aluno)   
   


  