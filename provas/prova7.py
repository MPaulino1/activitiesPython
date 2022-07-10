'''
Criar uma classe para armazenar as informações de um computador. O computador deve ter os seguintes atributos:

-Modelo
-Fabricante
-Processador
-Memória RAM
-Tamanho do HD
-Espaço ocupado do HD
-Está ligado?

Sua classe também deve ter os seguintes métodos:

-liga() -> altera o status de "Está ligado" para True
-desliga() -> altera o status de "Está ligado" para False
-limparHD() -> recebe por parâmetro o tamanho do espaço que deseja liberar do HD
-ocuparHD() -> recebe por parâmetro o tamanho do espaço que deseja ocupar do HD
'''

class Computador:
    def __init__(self, modelo, fabricante, processador, memoriaRam):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador = processador
        self.memoriaRam = memoriaRam
        self.tamHd = 100
        self.slotHd = 70
        self.ligado = False

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print('O computador está sendo ligado...')
        else:
            print('O computador já está ligado!')

    def desliga(self):
        if self.ligado:
            self.ligado = True
            print('Desligando o computador...')
        else:
            print('O computador já está desligado.')

    def limparHD(self, memoria):
        if self.slotHd - memoria <= self.tamHd:
            self.slotHd -= memoria
            print('Limpando...')
            print(self.slotHd)
        else:
            print('Valor incorreto')


    def ocuparHd(self, memoria):
        if self.slotHd + memoria <= self.tamHd:
            self.slotHd += memoria
            print('Adicionando arquivos....')
            print(self.tamHd)
        else:
            print('Excedeu o limite do HD')


pc1 = Computador('Inspiron', 'Dell', 'I5', 'R1000')

print(f'Computador modelo {pc1.modelo}, marca {pc1.fabricante}, processador {pc1.processador} e a memória {pc1.memoriaRam}.')

pc1.liga()
pc1.limparHD(50)
pc1.ocuparHd(101)


