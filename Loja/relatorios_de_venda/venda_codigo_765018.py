# codigo:765018   data:2022-05-27

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-27"

codigo = "765018"

# (loja)
loja = "Secound Test Store   "
cnpj = "4254"   
contato = "987987   "

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Erik Satoshi"    
cpf = "22233344460"    
telefone = "243425425"    
email = "erik@hot.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Toyota"    
nome = "Prius"    
ano = "2015"    
valor_avaliado = "70 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "65 000"

venda_765018 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



