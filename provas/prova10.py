class Aluno:
    def __init__(self, matricula, nome, idade, curso):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.curso = curso

class Escola:
    def __init__(self, nome, endereco, cursos):
        self.nome = nome
        self.endereco = endereco
        self.cursos = cursos
        self.alunos = []


    def matricular(self, aluno):
        self.alunos.append(aluno)

    def listarAlunos(self):
        for aluno in self.alunos:
            print(f'Matricula: {aluno.matricula}')
            print(f'Nome: {aluno.nome}')
            print(f'Idade: {aluno.idade}')
            print(f'Curso: {aluno.curso}')

escola = Escola('Infinity School', 'Av. Santos Dummont', ['Dev', 'Fotografia'])
# aluno = Aluno(1, 'José', 19, 'Dev')
# escola.matricular(aluno)
# escola.listarAlunos()

while True:
    opcao = int(input('Escola uma opção: \n'	
          '1 - Matricular Aluno \n'
          '2 - Exibir Alunos \n'
          '3 - Sair'))

    if opcao == 1:
        matricula = int(input('Informe a matricula: '))
        nome = input('Informe o nome do aluno: ')
        idade = int(input('Informe a idade do aluno: '))
        curso = input('Informe a curso do aluno: ')
        aluno = Aluno(matricula, nome, idade, curso)
        escola.matricular(aluno)
        print('aluno matriculado com sucesso!!')

    elif opcao == 2:
        escola.listarAlunos()

    elif opcao == 3:
        break

    else:
        print('Opção inválida!!')
