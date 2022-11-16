from estrutura.Venda import Venda

vendas_registradas = list()

codigos_de_vendas_existentes = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


# TESTE  !!!!!!!!
def add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo):
    codigo_int = int(codigo)
    codigos_de_vendas_existentes.append(codigo_int)


#  --------------  -----------   --------------   ------------- -----


# ((Dados da Venda)):

data = "2022-11-13"

codigo = "536368"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store

loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_de_funcionarios_registrados import funcionario_maria_souza8973542

funcionario = funcionario_maria_souza8973542

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_ayumi_souza98798798

cliente = cliente_ayumi_souza98798798

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_wolkswagen_gol_875414

carro = carro_wolkswagen_gol_875414

valor_negociado = "28000"

venda_536368 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)

add_venda_na_lista_do_main(venda_536368)


# teste   !!!!!!!!!!!
add_novo_codigo_na_lista_de_codigos_ja_existentes(venda_536368.codigo)


# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-11-13"

codigo = "477120"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store

loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_de_funcionarios_registrados import funcionario_jorge_monteiro9872984729

funcionario = funcionario_jorge_monteiro9872984729

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_erik_miyajima23434248979

cliente = cliente_erik_miyajima23434248979

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_wolkswagen_golf_520954

carro = carro_wolkswagen_golf_520954

valor_negociado = "19000"

venda_477120 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)

add_venda_na_lista_do_main(venda_477120)


# teste  !!!!!
add_novo_codigo_na_lista_de_codigos_ja_existentes(venda_477120.codigo)

# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-11-16"

codigo = "54407"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_de_funcionarios_registrados import funcionario_fabiana_junqueira987987
funcionario = funcionario_fabiana_junqueira987987

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_jose_silveira787979242
cliente = cliente_jose_silveira787979242

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_toyota_corolla_818630
carro = carro_toyota_corolla_818630

valor_negociado = "56000"

venda_54407 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_54407)
add_novo_codigo_na_lista_de_codigos_ja_existentes(venda_54407.codigo)

# -------------------------------------------------------

# ((Dados da Venda)):

data = "2022-11-16"

codigo = "20744"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_de_funcionarios_registrados import funcionario_maria_souza8973542
funcionario = funcionario_maria_souza8973542

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_erik_miyajima23434248979
cliente = cliente_erik_miyajima23434248979

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_fiat_uno_869338
carro = carro_fiat_uno_869338

valor_negociado = "35000"

venda_20744 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_20744)
add_novo_codigo_na_lista_de_codigos_ja_existentes(venda_20744.codigo)

# -------------------------------------------------------

# ((Dados da Venda)):

data = "2022-11-16"

codigo = "230990"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_de_funcionarios_registrados import funcionario_joao_silva98476538927
funcionario = funcionario_joao_silva98476538927

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_ayumi_souza98798798
cliente = cliente_ayumi_souza98798798

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_wokswagen_gol_125749
carro = carro_wokswagen_gol_125749

valor_negociado = "20000"

venda_230990 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_230990)
add_novo_codigo_na_lista_de_codigos_ja_existentes(venda_230990.codigo)

# -------------------------------------------------------


