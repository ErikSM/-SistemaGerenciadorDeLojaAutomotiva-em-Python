# codigo:614330   data:2022-05-29

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-29"

codigo = "614330"

# (loja)
loja = "Test Store   "
cnpj = "675"   
contato = "76565465   "

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Joao Batista"    
cpf = "827492749"    
telefone = "8798739"    
email = "ecoo@hsid.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "WolksWagen"    
nome = "Hilux"    
ano = "2010"    
valor_avaliado = "200 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "350 000"

venda_614330 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



