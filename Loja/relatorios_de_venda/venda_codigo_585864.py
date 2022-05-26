# codigo:585864   data:2022-05-26

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-26"

codigo = "585864"

# (loja)
loja = "Secound Test Store"
cnpj = "4254"
contato = "987987"

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Erik Satoshi"    
cpf = "22233344460"    
telefone = "243425425"    
email = "erik@hot.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Ferrari"    
nome = "Ferrari GP X"    
ano = "2013"    
valor_avaliado = "500 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "450 000"

venda_585864 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



