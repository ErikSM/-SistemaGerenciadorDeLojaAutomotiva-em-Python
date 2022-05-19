# codigo:684464   data:2022-05-19

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-19"

codigo = "684464"
#(loja)

loja = "Hachi Test Store"
cnpj = "098097"
contato = "053 2342"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Ayumi yuka"    
cpf = "2342342"    
telefone = "09032424"    
email = "fjwo@.com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "Toyota"    
nome = "MarkII100"    
ano = "12"    
valor_avaliado = "500000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "470 000"

venda_684464 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



