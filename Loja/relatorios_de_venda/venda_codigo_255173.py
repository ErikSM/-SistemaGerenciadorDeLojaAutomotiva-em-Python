# codigo:255173   data:2022-05-26

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda

# ((Dados da Venda)):

data = "2022-05-26"

codigo = "255173"

# (loja)
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
montadora = "Ferrari"
nome = "Ferrari GP X"
ano = "19"
valor_avaliado = "5 000 000"

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "4 000 000"

venda_255173 = Venda(data, codigo, loja, cliente, carro, valor_negociado)
