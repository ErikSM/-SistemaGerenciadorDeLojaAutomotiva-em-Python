# codigo:67103   data:2022-05-19

from estrutura.Carro import Carro
from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Venda import Venda

# ((Dados da Venda)):

data = "2022-05-19"

codigo = "67103"
# (loja)

loja = "Test Store"
cnpj = "2422"
contato = "2342"

loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Erik Satoshi"
cpf = "22233344460"
telefone = "243425425"
email = "erik@hot.com "

cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Toyota"
nome = "Prius"
ano = "22"
valor_avaliado = "1000000"

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_avaliado = "300 000"

venda_67103 = Venda(data, codigo, loja, cliente, carro, valor_avaliado)
