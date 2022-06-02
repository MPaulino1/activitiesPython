''''
Atividade
1.Crie uma classe chamada produto, que conterá código, nome e valor.
2. Crie uma classe chamada carrinho de compra que em seu construtor
inicializa-rá uma lista de produtos vazia
3. Um método para inserir produtos, que receberá um produto por
parâmetro e será inserido na lista.
4. Um métodos para listar todos os produtos.
5. Um método para exibir o valor total
'''

class Produto:
    def __init__(self, codigo, nome, valor):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor


class Carrinho:
    def __init__(self):
        self.lista = []

    def inserirProdutos(self, prod):
        prod = Produto(255, 'Arroz', 'R$ 5,00')
        car = Carrinho('555')
        self.lista.append(self.prod)

        print(car)

    def listarProdutos(self):
        for produtos in self.lista:
            print(f'Produto: {produtos}')

produto1 = Carrinho()
produto1.listarProdutos()