
class ContaBancaria:

    def __init__(self, titular, numeroDaConta, saldo, vip):
        self.titular = titular
        self.numeroDaConta = numeroDaConta
        self.saldo = saldo
        self.vip = vip


titular = input('Informe o titular da conta: ')
numeroDaConta = int(input('Informe o número da conta: '))
saldo = float(input('Informe o seu saldo: '))
vip = bool(input('Informe o VIP: '))

conta1 = ContaBancaria(titular, numeroDaConta, saldo, vip)

print(f'Seu saldo antigo: {conta1.saldo}')


conta1.saldo = 3000.50

print(f'Seu saldo novo: {conta1.saldo}')