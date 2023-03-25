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

data = "2023-01-03"

codigo = "384399"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_379018
funcionario = funcionario_379018

# (cliente)
from entrada_de_dados.lista_clientes import cliente_251752 
cliente = cliente_251752 

# (veiculo)
from entrada_de_dados.lista_carros import carro_873311
carro = carro_873311

valor_negociado = "75000"

venda_384399 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_384399, "venda_384399")


# -------------------------------------------------------


# ((Dados da Venda)):

data = "2023-01-03"

codigo = "387595"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_267707
funcionario = funcionario_267707

# (cliente)
from entrada_de_dados.lista_clientes import cliente_749240
cliente = cliente_749240

# (veiculo)
from entrada_de_dados.lista_carros import carro_988526
carro = carro_988526

valor_negociado = "47000"

venda_387595 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_387595, "venda_387595")


# -------------------------------------------------------


# ((Dados da Venda)):

data = "2023-03-19"

codigo = "678358"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_379018
funcionario = funcionario_379018

# (cliente)
from entrada_de_dados.lista_clientes import cliente_417257
cliente = cliente_417257

# (veiculo)
from entrada_de_dados.lista_carros import carro_719373
carro = carro_719373

valor_negociado = "250000"

venda_678358 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_678358, "venda_678358")


# -------------------------------------------------------


# ((Dados da Venda)):

data = "2023-03-25"

codigo = "33373"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_367715
funcionario = funcionario_367715

# (cliente)
from entrada_de_dados.lista_clientes import cliente_251752 
cliente = cliente_251752 

# (veiculo)
from entrada_de_dados.lista_carros import carro_827583
carro = carro_827583

valor_negociado = "0"

venda_33373 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_33373, "venda_33373")


# -------------------------------------------------------


# ((Dados da Venda)):

data = "2023-03-25"

codigo = "40082"

# (loja)
from entrada_de_dados.lista_lojas import loja_test_store
loja = loja_test_store

# (funcionario)
from entrada_de_dados.lista_funcionarios import funcionario_367715
funcionario = funcionario_367715

# (cliente)
from entrada_de_dados.lista_clientes import cliente_417257
cliente = cliente_417257

# (veiculo)
from entrada_de_dados.lista_carros import carro_492654
carro = carro_492654

valor_negociado = "15000"

venda_40082 = Venda(data, codigo, loja, funcionario, cliente, carro, valor_negociado)


add_venda_na_lista(venda_40082, "venda_40082")


# -------------------------------------------------------

