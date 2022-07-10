'''
Fazendo parte de um time de desenvolvedores, foi atribuído a você o desenvolvimento de um módulo de um sistema
de empresas que pagam tributos às prefeituras. Cada empresa cadastrada com o nome, cnpj, média de funcionários,
e média de lucro mensal. As prefeituras devem ser cadastradas com cidade, prefeito(a) e valor total de impostos.
O(a) prefeito(a) deve ser cadastrado também com nome, cpf e formação. A prefeitura pode ter várias empresas as
quais coleta impostos. Cada empresa deve fornecer 1.6% de seus lucros mensais para a prefeitura associada e deve
ser feito o cálculo a partir desta informação de todas as empresas de uma prefeitura, quanto pagam mensalmente,
pois este será o valor total de impostos.
'''


class Empresa:
    def __init__(self, nome, cnpj, medFuncionarios, medLucro):
        self.nome = nome
        self.cnpj = cnpj
        self.medFuncionarios = medFuncionarios
        self.medLucro = medLucro

    def calcularImposto(self):
        var = self.medLucro * 0.16
        print(var)

class Prefeitura:
    def __init__(self, cidade, prefeito, totalImpostos):
        self.cidade = cidade
        self.prefeito = prefeito
        self.totalImpostos = totalImpostos

class Prefeito:
    def __init__(self, nome, cpf, formacao):
        self.nome = nome
        self.cpf = cpf
        self.formacao = formacao

emp1 = Empresa('Adibas', 237, 5, 1500)
emp1.calcularImposto()