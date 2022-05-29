# codigo:590404   data:2022-05-27

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-27"

codigo = "590404"

# (loja)
loja = "Test Store   "
cnpj = "675"   
contato = "76565465   "

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Joao Batista"    
cpf = "827492749"    
telefone = "8798739"    
email = "ecoo@hsid.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Ferrari"    
nome = "Ferrari GP X"    
ano = "2013"    
valor_avaliado = "500 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "500 000"

venda_590404 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



