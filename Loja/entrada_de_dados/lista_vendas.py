from estrutura.Venda import Venda

vendas_registradas = list()

codigos_de_vendas_existentes = list()


def add_venda_na_lista(venda: Venda):
    vendas_registradas.append(venda)
    _add_novo_codigo_na_lista_de_codigos_ja_existentes(venda.codigo)


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo):
    codigo_int = int(codigo)
    codigos_de_vendas_existentes.append(codigo_int)


#  --------------  -----------   --------------   ------------- -----


# ((Dados da Venda)):

data = "2022-11-17"

codigo = "115167"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_batista_melo2384728974
funcionario = funcionario_batista_melo2384728974

# (cliente)
from entrada_de_dados.lista_clientes import cliente_ayumi_souza98798798
cliente = cliente_ayumi_souza98798798

# (veiculo)
from entrada_de_dados.lista_carros import carro_wolkswagen_gol_339991
carro = carro_wolkswagen_gol_339991

valor_negociado = "27000"

venda_115167 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_115167)


# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-11-17"

codigo = "27637"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_joao_silva98476538927
funcionario = funcionario_joao_silva98476538927

# (cliente)
from entrada_de_dados.lista_clientes import cliente_jose_silveira787979242
cliente = cliente_jose_silveira787979242

# (veiculo)
from entrada_de_dados.lista_carros import carro_toyota_hilux_377261
carro = carro_toyota_hilux_377261

valor_negociado = "175000"

venda_27637 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_27637)


# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-11-17"

codigo = "367251"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_fabiana_junqueira987987
funcionario = funcionario_fabiana_junqueira987987

# (cliente)
from entrada_de_dados.lista_clientes import cliente_erik_miyajima23434248979
cliente = cliente_erik_miyajima23434248979

# (veiculo)
from entrada_de_dados.lista_carros import carro_toyota_corolla_754655
carro = carro_toyota_corolla_754655

valor_negociado = "25000"

venda_367251 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_367251)


# -------------------------------------------------------

