'''
Atividade - Controle Remoto
Mudar de canal, aumentar e diminuir volume

Canais = (SBT, Globo, Record)
Valores = (1, 2, 3)

Volume = 0 à 20
Funções

Função mudar o canal :
1. Mudar de canal, muda para o canal acima, se estiver no ultimo canal volta para o primeiro

Funções aumentar e diminuir o volume
1. Aumentar o volume, incrementa em um o volume da TV, se estiver no volume máximo não pode permitir incrementar mais

2. Diminuir o volume, decrementa em um o volume da TV, se estiver no volume mínimo não poderá permitir diminuir mais.

3. Criar um menu para solicitar o que o usuário deseja fazer
Ex: 1 - Mudar canal, 2 - Aumentar volume 3 - Diminuir Volume 4 - Sair
'''

canal = 1
volume = 18

def mudarCanal():
    global canal

    if canal == 1:
        canal = 2
        print('Você está assistindo Fátima Bernardes')
    elif canal == 2:
        canal = 3
        print('Você está assistindo Fala que eu te escuto!')
    else:
        canal = 1
        print('Você está assistindo programa do Silvio Santos')

def aumentarVolume():
    global volume
    if volume == 20:
        print('Tá muito alto esse negócio!!')
    else:
        volume += 1
        print(f'Volume da TV: {volume}')

def diminuirVolume():
    global volume
if volume == 0:
    print('Da pra ouvir nada ')
else:
    volume -= 1
    print(f'Volume da TV: {volume}')

while True:
    print('Escolha uma opção')
    print('1 - Alterar Canal')
    print('2 - Aumentar volume')
    print('3 - Diminuir volume')
    print('4 - Desligar a TV')
    opcao = int(input('Selecione uma opção: '))

    if opcao == 1:
        mudarCanal()
    elif opcao == 2:

        aumentarVolume()

    elif opcao == 3:

        diminuirVolume()

    elif opcao == 4:
        print('Desligando...')
        break
    else:
        print('Opção inválida')
