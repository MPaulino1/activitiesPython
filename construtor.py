class Pessoa:

    # Método (função) construtor. Sempre será chamado quando um novo objeto é criado
    def __init__(self, nome, sexo, cpf): #self = fco

        #Atributos do objeto, sempre definidos através da palavra "self" + . + o nome do atributo
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = True


    def desativar(self):
        self.ativo = False
        print('Usuário desativado com sucesso!!!')



fco = Pessoa('Francisco', 'M', '012.231.123-12')

print(fco.cpf)
print(fco.nome)
print(fco.sexo)
print(fco.ativo)

fco.desativar()

print(fco.ativo)