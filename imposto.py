"""
Crie uma classe chamada Pessoa que conterá os atributos, estado, renda, imposto (inicializará com zero)
e um método chamado declarar impostos.

Crie uma classe PessoaFísica que herdará de pessoa, com os atributos nome, cpf, data de nascimento.
E seu método de declarar imposto irá verificar que caso sua renda seja superior a 2000,
seu imposto deverá ser 5% do valor da renda. Caso contrário o imposto da pessoa deve ser 0.

Crie uma classe PessoaJuridica que herdará de pessoa, com os atributos, cnpj, razão social, nome fantasia
e seu método de calcular imposto será 20% sobre o valor da renda da empresa.

Ao final do programa exiba todos os dados dos dois objetos e seus métodos de calcular o imposto.
"""


class Pessoa:
  def __init__(self, estado, renda):
   self.estado = estado
   self.renda = renda
   self.imposto = 0

  def declararImposto(self):
   pass


class PessoaFisica(Pessoa):
  def __init__(self, estado, renda, nome, cpf, dataNasc):
   super().__init__(estado, renda)
   self.nome = nome
   self.cpf = cpf
   self.dataNasc = dataNasc

  def declararImposto(self):
   if self.renda > 2000:
    self.imposto = self.renda - 0.05
    print(self.imposto)
   else:
    print('Não precisa declacar imposto.')

class PessoaJuridica(Pessoa):
   def __init__(self, estado, renda, cnpj, razaoSocial, nomeFantasia):
     super().__init__(estado, renda)
      self.cnpj = cnpj
      self.razSocial = razaoSocial
      self.nomeFantasia = nomeFantasia

   def declararImposto(self):
    self.imposto = self.renda * 0.2
    print(self.imposto)