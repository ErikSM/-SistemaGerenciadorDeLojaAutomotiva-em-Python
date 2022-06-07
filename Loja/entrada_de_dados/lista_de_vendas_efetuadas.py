from estrutura.Venda import Venda
from estrutura.Loja import Loja
from estrutura.Cliente import Cliente
from estrutura.Carro import Carro


vendas_registradas = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


#  --------------  -----------   --------------   ------------- -----


# ((Dados da Venda)):

data = "2022-05-29"

codigo = "698138"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store_3
loja = loja_test_store_3

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_aline_barros23424
cliente = cliente_aline_barros23424

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_toyota_prius_774811
carro = carro_toyota_prius_774811

valor_negociado = "340 000"

venda_698138 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_698138)

# -------------------------------------------------------


# ((Dados da Venda)):

data = "2022-06-05"

codigo = "541416"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_secound_test_store
loja = loja_secound_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_Erik_Satoshi22233344460
cliente = cliente_Erik_Satoshi22233344460

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_mazda_rx7_765597
carro = carro_mazda_rx7_765597

valor_negociado = "200 000"

venda_541416 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_541416)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-06-06"

codigo = "268077"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_secound_test_store
loja = loja_secound_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_joao_silva352
cliente = cliente_joao_silva352

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_fiat_uno_75705
carro = carro_fiat_uno_75705

valor_negociado = "24 000"

venda_268077 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_268077)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-06-07"

codigo = "794678"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_joao_silva352
cliente = cliente_joao_silva352

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_toyota_prius_1811
carro = carro_toyota_prius_1811

valor_negociado = "110 000"

venda_794678 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_794678)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-06-07"

codigo = "559874"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_Erik_Satoshi22233344460
cliente = cliente_Erik_Satoshi22233344460

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_fiat_uno_942082
carro = carro_fiat_uno_942082

valor_negociado = "50 000"

venda_559874 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_559874)

# -------------------------------------------------------


