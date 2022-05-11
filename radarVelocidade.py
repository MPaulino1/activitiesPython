'''
1. Função radar de velocidade
2. Parâmetros (velocidade do veiculo, limite de velocidade, placa)
3. Se a velocidade do veiculo estiver 20% acima do limite de velocidade
3a. Imprimir uma multa de 189,00
4. Se a velocidade estiver 50% acima do limite de velocidade
4a. Aplicar multa de 400,00
5. Se a velocidade estiver 80% acima do limite
5a. Aplicar multa de 989,00
6. Se estiver abaixo do limite, exibir uma mensagem informando que o veículo está ok
'''

def radar (velocidade, limite, placa):
    if velocidade > (limite * 0.2) + limite and velocidade < (limite * 0.5) + limite:
        print(f'Veículo placa {placa} foi multado em R$ 189,00')
    elif velocidade > (limite * 0.5) + limite and velocidade < (limite * 0.8) + limite:
        print(f'Veículo placa {placa} foi multado em R$ 400,00')
    elif velocidade > (limite * 0.8) + limite:
        print(f'Veículo placa {placa} foi multado em R$ 989,00')
    else:
        print(f'Veículo dentro da velocidade!!')

radar(80, 60,'OCR-9423')