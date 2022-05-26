# codigo:974793   data:2022-05-26

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-26"

codigo = "974793"

# (loja)
loja = "Test Store"
cnpj = "675"
contato = "76565465"

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Erik Satoshi"    
cpf = "22233344460"    
telefone = "243425425"    
email = "erik@hot.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Nissan"    
nome = "Skyline 35"    
ano = "2007"    
valor_avaliado = "300 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "250 000"

venda_974793 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



