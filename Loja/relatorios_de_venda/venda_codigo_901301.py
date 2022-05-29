# codigo:901301   data:2022-05-29

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-29"

codigo = "901301"

# (loja)
loja = "Test Store   "
cnpj = "675"   
contato = "76565465   "

loja = Loja(loja, cnpj, contato)

# (cliente)
nome = "Ayumi Souza"    
cpf = "2342"    
telefone = "23232432"    
email = "kljslf@.com"    

cliente = Cliente(nome, cpf, telefone, email)

# (veiculo)
montadora = "WolksWagen"    
nome = "Golf"    
ano = "2013"    
valor_avaliado = "60 000"    

carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "50 000"

venda_901301 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



