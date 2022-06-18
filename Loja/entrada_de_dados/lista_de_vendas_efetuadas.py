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


