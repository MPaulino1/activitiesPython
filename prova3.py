# preciso da soma e da media
num = 0
soma = 0
media = 0
cont = 0
while num != 2022:
	num = int(input('Digite um valor ou 2022 para encerrar o programa: '))
	if num != 2022:
		soma += num
		cont += 1
		media = soma/cont

print(f'A soma dos números é de {soma}, e a média é {media}.')
