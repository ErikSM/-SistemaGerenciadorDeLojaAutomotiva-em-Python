from estrutura.Venda import Venda


vendas_registradas = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


#  --------------  -----------   --------------   ------------- -----


# ((Dados da Venda)):

data = "2022-06-18"

codigo = "155920"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_erik_miyajima897498274
cliente = cliente_erik_miyajima897498274

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_wolkswagen_golf_gti_570752
carro = carro_wolkswagen_golf_gti_570752

valor_negociado = "23 000"

venda_155920 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_155920)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-06-19"

codigo = "6084"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_erik_miyajima897498274
cliente = cliente_erik_miyajima897498274

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_fiat_uno_561718
carro = carro_fiat_uno_561718

valor_negociado = "16 000"

venda_6084 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_6084)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-06-19"

codigo = "393755"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_ayumi_souza234299
cliente = cliente_ayumi_souza234299

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_toyota_lexus_856048
carro = carro_toyota_lexus_856048

valor_negociado = "80 000"

venda_393755 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_393755)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-06-24"

codigo = "907758"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_erik_miyajima897498274
cliente = cliente_erik_miyajima897498274

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_toyota_hilux_371922
carro = carro_toyota_hilux_371922

valor_negociado = "250 000"

venda_907758 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_907758)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-06-24"

codigo = "687154"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_ayumi_souza234299
cliente = cliente_ayumi_souza234299

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_toyota_prius_55076
carro = carro_toyota_prius_55076

valor_negociado = "120 000"

venda_687154 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_687154)

# -------------------------------------------------------


