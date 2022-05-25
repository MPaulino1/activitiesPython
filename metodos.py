'''
Criar uma classe de Carro, que corre até no máximo 120km/h. O carro deve ser cadastrado com marca,
modelo, ano, velocidade, se está ligado ou não e se é automático ou não.
O carro deve conter funcionalidades de:
- ligar
- Acelerar: apenas se o carro estiver ligado (uma quantidade que não passe da velocidade máxima
de 120.
- desligar
- verificarMacha com as regras abaixo:
- 1a marcha: 0 a 20km
- 2a marcha: ao atingir 20 km/h;
- 3a marcha: entre 30 e 35 km/h;
- 4a marcha: entre 45 e 50 km/h; e.
- 5a marcha: acim de 60 km/h.
'''

class Carro:
    def __init__(self, marca, modelo, ano, automatico):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        self.velocidadeMax = 120
        self.ligado = False

        if automatico == 'sim':
            self.automatico = True
        else:
            self.automatico = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print('O carro está ligado....')
        else:
            print('O carro já está ligado!!! VRUMMMM!!!')

    def acelerar(self, velocidade):
        if self.ligado == True and velocidade <= self.velocidadeMax:
            self.velocidade = velocidade
            print('Acelerando...')
            print(f'Velocidade atual: {self.velocidade}')
        else:
            print('A velocidade é muito alta ou o carro não está ligado!!')

    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            print('Desligado x_x')
        else:
            print('O carro já está desligado!!!')

    def verificarMarcha(self):
        if self.velocidade <= 20:
            print('Primeira Marcha!!')
        elif self.velocidade >20 and self.velocidade <= 30:
            print('Segunda Marcha!!')
        elif self.velocidade > 30 and self.velocidade <= 45:
            print('Terceira Marcha!!')
        elif self.velocidade > 45 and self.velocidade <= 60:
            print('Quarta Marcha!!!')
        else:
            print('Quinta marcha!!!!')



volks = Carro('Volkswagen', 'Gol 1.0', 2018, 'sim')

print(f'Marca: {volks.marca}')
print(f'Modelo: {volks.modelo}')
print(f'Ano: {volks.ano}')
print(f'Velocidade Atual: {volks.velocidade}')
print(f'Velocidade Máxima: {volks.velocidadeMax}')
print(f'Automático: {volks.automatico}')
print(f'Ligado: {volks.ligado}')
print(f'-----------------------------------------')

volks.ligar()
volks.acelerar(61)
volks.verificarMarcha()
volks.desligar()
