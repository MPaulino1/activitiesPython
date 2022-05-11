#Criando lista

def CriarLista():
     lista = []
     for i in range(5):
         x = input('Informe um valor: ')
         lista.append(x)
     print(f'Itens da lista: {lista}')

CriarLista()