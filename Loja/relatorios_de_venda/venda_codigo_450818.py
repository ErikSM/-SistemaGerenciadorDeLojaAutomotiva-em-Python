# codigo:450818   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-19"

codigo = "450818"
#(loja)

loja = "Five Test Store"
cnpj = "242525"
contato = "053 9868768"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Maria da Silva"    
cpf = "234235"    
telefone = "345345"    
email = "sef@.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Toyota"    
nome = "Prius"    
ano = "22"    
valor_avaliado = "1000000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "320 000"

venda_450818 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



