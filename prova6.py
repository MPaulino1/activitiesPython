def Asteroide():
    lista = []
Asteroide()

while True:
    opc = input('Tenho as últimas 5 distâncias da Terra dos asteroides: PALAS e VESTA. \n'
                'Digite o nome do asteroide para saber as distâncias registradas: ')
    if opc == 'PALAS':
        lista = ['848 mil km', '498 mil km', '468 mil km', '407 mil km', '326 mil km']
        print(lista)

    elif opc == 'VESTA':
        lista = ['316 mil km', '302 mil km', '260 mil km', '237 mil km', '222 mil km']
        print(lista)

    else:
        print('Opção incorreta.')

