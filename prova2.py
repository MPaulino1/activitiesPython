#prova2

day = int(input('Digite seu dia de nascimento: '))
month = int(input('Digite o número do seu mês de nascimento: '))

if day >= 21 and day <= 31 and month == 3 or day >= 1 and day <= 20 and month == 4:
    print('Áries')
elif day >= 21 and day <= 30 and month == 4 or day >= 1 and day <= 20 and month == 5:
    print('Touro')

elif day >= 21 and day <= 31 and month == 5 or day >= 1 and day <= 20 and month == 6:
    print('Gêmeos')

elif day >= 21 and day <= 31 and month == 6 or day >= 1 and day <= 22 and month == 7:
    print('Câncer')

elif day >= 23 and day <= 31 and month == 7 or day >= 1 and day <= 22 and month == 8:
    print('Leão')

elif day >= 23 and day <= 31 and month == 8 or day >= 1 and day <= 22 and month == 9:
    print('Virgem')

elif day >= 23 and day <= 31 and month == 9 or day >= 1 and day <= 22 and month == 10:
    print('Libra')

elif day >= 23 and day <= 31 and month == 10 or day >= 1 and day <= 21 and month == 11:
    print('Escorpião')

elif day >= 22 and day <= 31 and month == 11 or day >= 1 and day <= 21 and month == 12:
    print('Sagitário')

elif day >= 22 and day <= 31 and month == 12 or day >= 1 and day <= 20 and month == 1:
    print('Capricórnio')

elif day >= 21 and day <= 31 and month == 1 or day >= 1 and day <= 18 and month == 2:
    print('Aquário')

elif day >= 19 and day <= 28 and month == 2 or day >= 1 and day <= 20 and month == 3:
    print('Peixes')
else:
    print('Digite os dados corretamente!')