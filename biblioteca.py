'''
Crie uma classe chamada biblioteca, com atributos

- nome
- capacidade de livros
- localização
- livros = []

 - crie seus métodos acessores (getters e setters)

- Crie um método para adicionar livro (O nome do livro vai ser passado por parâmetro e adicionado a lista de livros)

- A quantidade de livros na lista não pode ser maior que a capacidade de livros da biblioteca

- Crie um método para exibir todos os livros
'''

class Biblioteca:
    def __init__(self):
        self.__nome = ""
        self.__capacidade = 0
        self.__localizacao = ""
        self.__livros = []

    #GETTERS E SETTERS
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade

    def getCapacidade(self):
        return self.__capacidade

    def setLocalizacao(self, localizacao):
        self.__localizacao = localizacao

    def getLocalizacao(self):
        return self.__localizacao

    def adicionarLivro(self, livro):
        if len(self.__livros) < self.__capacidade:
            self.__livros.append(livro)
            print(f'O livro {livro} foi adicionado a biblioteca!!')
        else:
            print('Já atingimos a nossa capacidade!!')

    def listarLivros(self):
        print('-------- Nossa lista de livros --------')
        for livro in self.__livros:
            print(f'Título do livro: {livro}')


saraiva = Biblioteca()
saraiva.setNome('Saraiva')
saraiva.setLocalizacao('Shopping Iguatemi')
saraiva.setCapacidade(3)
saraiva.adicionarLivro('Don Casmuro')
saraiva.adicionarLivro('Harry Potter')
saraiva.adicionarLivro('O Senhor dos Aneis')
saraiva.adicionarLivro('O Senhor dos Aneis - As duas Torres')
saraiva.listarLivros()
print('----------------------------------------\n\n')
print(f'Nome: {saraiva.getNome()}')
print(f'Endereço: {saraiva.getLocalizacao()}')
print(f'Capacidade: {saraiva.getCapacidade()}')