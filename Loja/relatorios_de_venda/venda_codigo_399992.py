# codigo:399992   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-19"

codigo = "399992"
#(loja)

loja = "Test Store"
cnpj = "2422"
contato = "2342"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Astrogildo Souza"    
cpf = "3453453"    
telefone = "0907657657"    
email = "sdfsf@.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Subaru"    
nome = "WRX"    
ano = "15"    
valor_avaliado = "500000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "870 000"

venda_399992 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



