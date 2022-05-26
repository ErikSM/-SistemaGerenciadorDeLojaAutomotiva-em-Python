# codigo:875655   data:2022-05-26

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-26"

codigo = "875655"

# (loja)
loja = "Store Test 3"
cnpj = "324"
contato = "4525"

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Joao Batista"    
cpf = "827492749"    
telefone = "8798739"    
email = "ecoo@hsid.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "Ferrari"    
nome = "Ferrari GP X"    
ano = "2013"    
valor_avaliado = "500 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "550 000"

venda_875655 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



