# codigo:294497   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda

# ((Dados da Venda)):

data = "2022-05-19"

codigo = "294497"
# (loja)

loja = "Quarta Test Store"
cnpj = "245252"
contato = "053 453453"

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

valor_negociado = "700 000"

venda_294497 = Venda(data, codigo, loja, cliente, carro, valor_negociado)
