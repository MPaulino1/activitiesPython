#Gerar média

def gerarMedia():
    lista = []
    for i in range(3):
        nota = float(input('Informe a nota: '))
        lista.append(nota)
    media = sum(lista) / len(lista)
    print(f'Média final: {media}')

gerarMedia()
