# codigo:249414   data:2022-05-22

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-22"

codigo = "249414"
#(loja)

loja = "Five Test Store"
cnpj = "2341"
contato = "3414"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Ayumi Barbara"    
cpf = "8768687"    
telefone = "090876876"    
email = "ayumi@xx.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Toyota"    
nome = "MarkII100"    
ano = "12"    
valor_avaliado = "500000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "500 000"

venda_249414 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



