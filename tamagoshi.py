'''
ATIVIDADE
Classe Bichinho Virtual:
Crie uma classe que modele um Tamagoshi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade.
Métodos: Alterar Nome, Fome, Saúde e Idade;
 Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagoshi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

class Tamagoshi:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__saude = 0
        self.__fome = 0

    def setNome(self,nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setSaude(self, saude):
        self.__saude = saude

    def getSaude(self):
        return self.__saude

    def setIdade(self, idade):
        self.__idade = idade

    def getIdade(self):
        return self.__idade

    def setFome(self, fome):
        self.__fome = fome

    def getFome(self):
        return self.__fome

    def humor(self):
        if self.__fome >= 80 and self.__saude >= 80:
            print('Estou feliz')

        elif self.__fome > 50 and self.__saude > 50:
            print('Estou zangado')
        elif self.__fome >25 and self.__saude > 25:
            print('Estou morrendo... :(')
        else:
            print('RIP Tamagoshi x_x')


fuleco = Tamagoshi()

fuleco.setNome('Fuleco')
fuleco.setIdade(2)
fuleco.setFome(20)
fuleco.setSaude(20)

print(fuleco.getSaude())
print(fuleco.getFome())
fuleco.humor()