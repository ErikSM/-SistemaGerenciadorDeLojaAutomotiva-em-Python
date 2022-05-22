# codigo:943684   data:2022-05-22

from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Carro import Carro
from estrutura.Venda import Venda


# ((Dados da Venda)):

data = "2022-05-22"

codigo = "943684"
#(loja)

loja = "haha"
cnpj = "sjfaoj"
contato = "23424"


loja = Loja(loja, cnpj, contato)
# (cliente)

nome = "Gloria da Silva"    
cpf = "25452"    
telefone = "235242"    
email = "dfssf@com "   


cliente = Cliente(nome, cpf, telefone, email)
# (veiculo)

montadora = "WolksWagen"    
nome = "Fuska"    
ano = "2"    
valor_avaliado = "50 000"    


carro = Carro(montadora, nome, ano, valor_avaliado)

valor_negociado = "70 000"

venda_943684 = Venda(data, codigo, loja, cliente, carro, valor_negociado)



