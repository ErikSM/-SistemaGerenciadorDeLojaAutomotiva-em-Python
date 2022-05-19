# codigo:820045   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-19"

codigo = "820045"
#(loja)

loja = "Test Store"
cnpj = "2422"
contato = "2342"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Ayumi Barbara"    
cpf = "8768687"    
telefone = "090876876"    
email = "ayumi@xx.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Ferrari"    
nome = "FerrariX"    
ano = "26"    
valor_avaliado = "4000000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "1 000 000"

venda_820045 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



