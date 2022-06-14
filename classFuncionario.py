'''
O gerente agora terá mais dois atributos. O setor que ele gerencia e sua comissão.
Além disso ele terá dois métodos, um de contratar que recebe a quantidade de funcionários do setor.
E será verificado se a quantidade for abaixo de 10, informar que serão contratados funcionários,
senão, informar que o setor tem gente o suficiente E o estagiário terá um novo atributo que serão as horas estagiadas.
O estagiário também terá um método de contratação. Onde será verificado nessa função se suas horas estagiadas
são acima de 300, caso sim. Informar que o estagiário será contratado. Senão informar que o estágio ainda não acabou.
'''



class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario

    def exibirDados(self):
        print(f'Nome: {self.nome}')
        print(f'Matrícula: {self.matricula}')
        print(f'Salário: {self.salario}')
        print('------------------\n')

class Gerente(Funcionario):
    def __init__(self, matricula, nome, salario, setor, comissao):
        self.setor = setor
        self.comissao = comissao
        super().__init__(matricula, nome, salario)

    def exibirDados(self):
        print(f'Setor: {self.setor}')
        print(f'Comissão: {self.comissao}')
        super().exibirDados()
        print('------------------\n')

    def contratar(self, qtd):
        if qtd < 10:
            print('Serão contratados mais funcionários')
        else:
            print('Setor com gente suficiente!')

class Estagiario(Funcionario):
    def __init__(self, matricula, nome, salario, horas):
        self.horas = horas
        super().__init__(matricula, nome, salario)

    def exibirDados(self):
        print(f'Quantidade de horas: {self.horas}')
        super().exibirDados()

    def contratarEstagiario(self):
        if self.horas > 300:
            print('Parabéns, você será contratado!!!')
        else:
            print('Seu estágio ainda não acabou!')

est = Estagiario('253', 'Rafael','R$ 800,00', 280)
ger = Gerente('154', 'João', 'R$ 2.500,00', 'Construção', 'R$ 500')

est.exibirDados()
ger.exibirDados()

est.contratarEstagiario()
ger.contratar(10)