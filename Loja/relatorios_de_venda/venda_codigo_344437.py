# codigo:344437   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-19"

codigo = "344437"
#(loja)

loja = "Setima Test Store"
cnpj = "4525"
contato = "053 9872242"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Fabielle Souza"    
cpf = "234223435"    
telefone = "345345"    
email = "sef@.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Toyota"    
nome = "Alphard"    
ano = "22"    
valor_avaliado = "300000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "900 000"

venda_344437 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



