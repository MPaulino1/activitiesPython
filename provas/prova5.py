'''
Escreva uma função que recebe um determinado ano e retorne o século daquele ano.
Exemplo:
Entrada -> 1453
Saída   -> XV
'''

def seculo(ano):
    if ano > 1 and ano <= 100:
        return 'I'
    elif ano > 100 and ano <= 200:
        return 'II'
    elif ano > 200 and ano <= 300:
        return 'III'
    elif ano > 300 and ano <= 400:
        return 'IV'
    elif ano > 400 and ano <= 500:
        return 'V'
    elif ano > 500 and ano <= 600:
        return 'VI'
    elif ano > 600 and ano <= 700:
        return 'VII'
    elif ano > 700 and ano <= 800:
        return 'VIII'
    elif ano > 800 and ano <= 900:
        return 'IX'
    elif ano > 900 and ano <= 1000:
        return 'X'
    elif ano > 1000 and ano <= 1100:
        return 'XI'
    elif ano > 1100 and ano <= 1200:
        return 'XII'
    elif ano > 1200 and ano <= 1300:
        return 'XIII'
    elif ano > 1300 and ano <= 1400:
        return 'XIV'
    elif ano > 1400 and ano <= 1500:
        return 'XV'
    elif ano > 1500 and ano <= 1600:
        return 'XVI'
    elif ano > 1600 and ano <= 1700:
        return 'XVII'
    elif ano > 1700 and ano <= 1800:
        return 'XVIII'
    elif ano > 1800 and ano <= 1900:
        return 'XIX'
    elif ano > 1900 and ano <= 2000:
        return 'XX'
    elif ano > 2000 and ano <= 2100:
        return 'XXI'
    else:
        return 'Valor inválido!'

ano = int(input('Digite o ano: '))
result = seculo(ano)
print(result)