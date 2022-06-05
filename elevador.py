class Elevador:
    def __init__(self, qtd_andares, andar_atual, capacidade, qtd_pessoas):
        self.qtd_andares = qtd_andares
        self.andar_atual = andar_atual
        self.capacidade = capacidade
        self.qtd_pessoas = qtd_pessoas


    def subir(self):
        if self.andar_atual < self.qtd_andares:
            self.andar_atual += 1
            print('Subindo...')
            print(f'Andar atual: {self.andar_atual}')

        else:
            print('Já estamos no ultimo andar...')

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print('Descendo...')
            print(f'Andar atual: {self.andar_atual}')
        else:
            print('Já estamos no térreo')

    def entrar(self, quantidade):
        if self.qtd_pessoas + quantidade <= self.capacidade:
            self.qtd_pessoas += quantidade
            print('Entrando...')
            print(f'Quantidade de pessoas no elevador: {self.qtd_pessoas}')
            print(f'Capacidade do elevador: {self.capacidade}')
        else:
            print('A capacidade ficará acima da permitida')

    def sair(self, quantidade):
        if self.qtd_pessoas - quantidade >= 0:
            self.qtd_pessoas -= quantidade
            print('Saindo...')
            print(f'Quantidade de pessoas no elevador: {self.qtd_pessoas}')
            print(f'Capacidade do elevador: {self.capacidade}')
        else:
            print('A quantidade de pessoas no elevador não pode ser negativa')



plaza_tower = Elevador(10, 2, 10, 5)

#subindo
plaza_tower.subir()
plaza_tower.subir()
plaza_tower.subir()
#Andar 5 no final


#descendo
plaza_tower.descer()
plaza_tower.descer()
plaza_tower.descer()
#Andar final 2

#entrando
plaza_tower.entrar(3)
#Quantidade de pessoas 8

#Saindo
plaza_tower.sair(6)
#Quantidade de pessoas 2