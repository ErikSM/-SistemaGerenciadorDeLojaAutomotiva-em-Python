# codigo:259100   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-19"

codigo = "259100"
#(loja)

loja = "Five Test Store"
cnpj = "242525"
contato = "053 9868768"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Fabielle Souza"    
cpf = "234223435"    
telefone = "345345"    
email = "sef@.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Toyota"    
nome = "MarkII100"    
ano = "12"    
valor_avaliado = "500000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "530 000"

venda_259100 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



