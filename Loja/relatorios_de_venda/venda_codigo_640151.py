# codigo:640151   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-19"

codigo = "640151"
#(loja)

loja = "Mega Test Store"
cnpj = "234234"
contato = "32424323"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Joao Batista"    
cpf = "827492749"    
telefone = "8798739"    
email = "ecoo@hsid.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Toyota"    
nome = "Prius"    
ano = "22"    
valor_avaliado = "1000000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "800 000"

venda_640151 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



