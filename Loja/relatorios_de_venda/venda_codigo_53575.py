# codigo:53575   data:2022-05-29

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-29"

codigo = "53575"

# (loja)
loja = "Four Store Test   "
cnpj = "2552"   
contato = "435252   "

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Aline Souza"    
cpf = "24242"    
telefone = "24544"    
email = "sjfslk@com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Ford"    
nome = "Fusion"    
ano = "2010"    
valor_avaliado = "90 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "130 000"

venda_53575 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



