# codigo:209604   data:2022-05-27

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-27"

codigo = "209604"

# (loja)
loja = "Secound Test Store   "
cnpj = "4254"   
contato = "987987   "

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Ayumi Souza"    
cpf = "2342"    
telefone = "23232432"    
email = "kljslf@.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Nissan"    
nome = "Skyline 35"    
ano = "2007"    
valor_avaliado = "300 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "200 000"

venda_209604 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



