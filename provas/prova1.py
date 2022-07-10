#Lógica de Programação

tempoGasto = float(input('Quantas horas durou a viagem? '))
velocidadeMedia = float(input('Qual sua velocidade média? '))
distancia = tempoGasto*velocidadeMedia
litros_usados = distancia/12

print('A velocidade média do veículo é de', velocidadeMedia, 'km/h.')
print('O tempo gasto na viagem é de', tempoGasto, 'horas.')
print( 'A distância percorrida é de', distancia, 'Km.')
print('E a quantidade de litros gastos na viagem:', litros_usados,'litros.')