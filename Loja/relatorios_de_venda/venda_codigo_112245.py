# codigo:112245   data:2022-05-26

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-26"

codigo = "112245"

#(loja)
loja = "Test Store"
cnpj = "675"
contato = "76565465"


loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Ayumi Barbara"   
cpf = "8768687"   
telefone = "090876876"   
email = "ayumi@xx.com"   

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "WolksWagen"   
nome = "Fuska"   
ano = "2"   
valor_avaliado = "100 000"   


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "90 000"

venda_112245 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



