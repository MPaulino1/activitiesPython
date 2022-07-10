'''
Você foi convidado a desenvolver um sistema para registro de um estacionamento,
onde mantém informações sobre os veículos que entram e saem do local. Os veículos
são cadastrados com tipo do veículo (carro, moto, caminhão, etc.), placa, modelo,
data e horário de entrada e data e horário de saída, com um valor total a pagar.
O sistema deve receber como input o valor da hora e só deve atribuir o total a pagar
no momento que receber a informação do horário de saída, que não é obrigatório inserir na hora do registro
 do veículo. Para isso, deve-se encapsular todos os atributos e ter mapeado a regra que a saída do veículo
não poderá ser mais antiga que a entrada dele no estacionamento.
'''

class Veiculo:
    def __init__(self, tipo, valor, placa, modelo, entrada, hentrada, hsaida=0, status='Estacionando'):
        self.__tipo = tipo
        self.__valor = valor
        self.__placa = placa
        self.__modelo = modelo
        self.__entrada = entrada
        self.__hentrada = hentrada
        self.__hsaida = hsaida
        self.__status = status

    @property
    def placa(self):
        return self.__placa

    def mostraVeiculo(self):
        print(f'\nTipo: {self.__tipo}')
        print(f'Placa: {self.__placa}')
        print(f'Modelo: {self.__modelo}')
        print(f'Entrada: {self.__entrada}')
        print(f'Status: {self.__status}')

    def registraSaida(self, hsaida):
        self.__hsaida = hsaida
        htotal = self.__hsaida - self.__hentrada
        total = htotal * self.__valor
        self.__status = 'VEÍCULO SAIU DO ESTACIONAMENTO'
        print(f'O valor total a pagar é de R$: {total:.2f}')


def inicial():
    lista = []

while True:
    t = 'n'
    inicial()
    var = int(input('Informe a opção desejada: 1 - Moto | 2 - Carro | 3 - Caminhão | 4 - Verificar | 5 - Placa | 6 - Retirar Veículo | 0 - Sair: '))
    if var == 1:
        tipo = 'Moto'
        valor = 2.0
    elif var == 2:
        tipo = 'Carro'
        valor = 5.0
    elif var == 3:
        tipo = 'Caminhão'
        valor = 8.0
    elif var == 4:
        for veic in lista:
            veic.mostraVeiculo()
            t = 's'
        if t == 'n':
            print('Nenhum veículo encontrado!')
        a = input('')
        continue
    elif var == 5:
        pesquisa = input('Informe a placa do veículo: ')
        for veic in lista:
            if pesquisa == veic.placa:
                veic.mostraVeiculo()
                t = 's'
        if t == 'n':
            print('Nenhum veículo encontrado!')
        a = input('')
        continue
    elif var == 6:
        pesquisa = input('Informe a placa do veículo: ')
        for veic in lista:
            if pesquisa == veic.placa:
                t = 's'
                saida = input('Informe a hora da saída (hh:mm): ')
                horas = []
                for i in saida:
                    horas.append(i)
                hsaida = float(horas[0] + horas[1])
                if hsaida < hentrada or hsaida > 24:
                    print('Horário inválido!')
                    continue
                msaida = float(horas[3] + horas[4])
                if msaida > 0:
                    hsaida += 1
                total = veic.registraSaida(hsaida)
        if t == 'n':
            print('Nenhum veículo encontrado!')
        a = input('')
        continue

    elif var == 0:
        break
    else:
        print('Opção inválida!')
        continue

    placa = input(f'Informe a placa: ')
    modelo = input(f'Qual o modelo: ')
    data = input('Data da entrada (dd/mm): ')
    entrada = input('Informe a hora da entrada (hh:mm): ')
    horae = []
    for i in entrada:
        horae.append(i)
    hentrada = int(horae[0] + horae[1])
    if hentrada > 24:
        print('Horário inválido!')
        continue

veiculo = Veiculo(tipo, valor, placa, modelo, data, entrada, hentrada)
lista.append(veiculo)

print('Fim de acesso!')