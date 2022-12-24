from estrutura.Venda import Venda

vendas_registradas = list()

codigos_de_vendas_existentes = list()


def add_venda_na_lista(venda: Venda, variavel):
    venda.nome_da_variavel = variavel
    venda.funcionario.comissoes_recebidas.append(float(venda.comissao_sobre_a_venda))
    venda.funcionario.total_comissoes_recebidas += float(venda.comissao_sobre_a_venda)
    vendas_registradas.append(venda)
    _add_novo_codigo_na_lista_de_codigos_ja_existentes(venda.codigo)


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo):
    codigo_int = int(codigo)
    codigos_de_vendas_existentes.append(codigo_int)


#  --------------  -----------   --------------   ------------- -----


# ((Dados da Venda)):


# ((Dados da Venda)):

data = "2022-12-02"

codigo = "120550"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store

loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_armando_silveira88776540902

funcionario = funcionario_armando_silveira88776540902

# (cliente)
from entrada_de_dados.lista_clientes import cliente_erik_miyajima23948729487

cliente = cliente_erik_miyajima23948729487

# (veiculo)
from entrada_de_dados.lista_carros import carro_toyota_corolla_78502

carro = carro_toyota_corolla_78502

valor_negociado = "63000"

venda_120550 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)

add_venda_na_lista(venda_120550, "venda_120550")

# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-12-03"

codigo = "949530"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store

loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_armando_silveira88776540902

funcionario = funcionario_armando_silveira88776540902

# (cliente)
from entrada_de_dados.lista_clientes import cliente_ayumi_mello32489765098

cliente = cliente_ayumi_mello32489765098

# (veiculo)
from entrada_de_dados.lista_carros import carro_wolkswagen_golf_942353

carro = carro_wolkswagen_golf_942353

valor_negociado = "39000"

venda_949530 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)

add_venda_na_lista(venda_949530, "venda_949530")

# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-12-03"

codigo = "786778"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store

loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_joao_pereira77832209823

funcionario = funcionario_joao_pereira77832209823

# (cliente)
from entrada_de_dados.lista_clientes import cliente_erik_miyajima23948729487

cliente = cliente_erik_miyajima23948729487

# (veiculo)
from entrada_de_dados.lista_carros import carro_wolkswagon_gol_988526

carro = carro_wolkswagon_gol_988526

valor_negociado = "70000"

venda_786778 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)

add_venda_na_lista(venda_786778, "venda_786778")

# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-12-04"

codigo = "854985"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store

loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_joao_pereira77832209823

funcionario = funcionario_joao_pereira77832209823

# (cliente)
from entrada_de_dados.lista_clientes import cliente_erik_miyajima23948729487

cliente = cliente_erik_miyajima23948729487

# (veiculo)
from entrada_de_dados.lista_carros import carro_toyota_hilux_679209

carro = carro_toyota_hilux_679209

valor_negociado = "400000"

venda_854985 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)

add_venda_na_lista(venda_854985, "venda_854985")

# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-12-09"

codigo = "937931"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store

loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_ana_julia98767823490

funcionario = funcionario_ana_julia98767823490

# (cliente)
from entrada_de_dados.lista_clientes import cliente_ayumi_mello32489765098

cliente = cliente_ayumi_mello32489765098

# (veiculo)
from entrada_de_dados.lista_carros import carro_wolkswagen_gol_492654

carro = carro_wolkswagen_gol_492654

valor_negociado = "13000"

venda_937931 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)

add_venda_na_lista(venda_937931, "venda_937931")

# -------------------------------------------------------
