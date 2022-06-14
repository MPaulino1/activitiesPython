
class Endereco:
    def __init__(self, rua, bairro, cidade):
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade


class Empresa:
    def __init__(self, nome, area):
        self.__nome = nome
        self.__area = area
        self.enderecos = []

    def inserir_endereco(self, rua, bairro, cidade):
        self.obj = Endereco(rua, bairro, cidade)
        self.enderecos.append(self.obj)

    def listarEnderecos(self):
        print('Endereços da Empresa: \n')
        for endereco in self.enderecos:
            print(f'Rua: {endereco.rua}')
            print(f'Bairro: {endereco.bairro}')
            print(f'Cidade: {endereco.cidade}')

    def exibirDados(self):
        print(f'Nome da Empresa: {self.__nome}')
        print(f'Area da Empresa: {self.__area}')
        print('------------------------------ ')

emp1 = Empresa('Oscorp', 'Tecnologia')
emp1.inserir_endereco('20', 'Aldeota', 'Fortaleza')
emp1.inserir_endereco('565', 'Maraponga', 'Fortaleza')
emp1.exibirDados()
emp1.listarEnderecos()
