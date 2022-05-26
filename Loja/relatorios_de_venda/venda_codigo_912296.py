# codigo:912296   data:2022-05-26

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-26"

codigo = "912296"

#(loja)
loja = "Test Store"
cnpj = "675"
contato = "76565465"


loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Maria da Silva"   
cpf = "234235"   
telefone = "345345"   
email = "sef@.com"   

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Toyota"   
nome = "Prius"   
ano = "25"   
valor_avaliado = "700 000"   


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "600 000"

venda_912296 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



