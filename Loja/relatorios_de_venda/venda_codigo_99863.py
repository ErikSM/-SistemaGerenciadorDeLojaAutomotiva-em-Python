# codigo:99863   data:2022-05-26

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-26"

codigo = "99863"

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
montadora = "Nissan"   
nome = "Skyline 35"   
ano = "22"   
valor_avaliado = "3 000 000"   


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "300 000"

venda_99863 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



