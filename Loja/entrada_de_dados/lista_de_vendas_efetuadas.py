from estrutura.Venda import Venda


vendas_registradas = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


#  --------------  -----------   --------------   ------------- -----


# ((Dados da Venda)):

data = "2022-11-02"

codigo = "124776"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_erik_miyajima23434248979
cliente = cliente_erik_miyajima23434248979

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_wolkswagen_gol_875414
carro = carro_wolkswagen_gol_875414

valor_negociado = "25000"

venda_124776 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_124776)

# -------------------------------------------------------



# ((Dados da Venda)):

data = "2022-11-02"

codigo = "596013"

# (loja)
from entrada_de_dados.lista_de_lojas_criadas import loja_test_store
loja = loja_test_store

# (cliente)
from entrada_de_dados.lista_de_clientes_registrados import cliente_ayumi_souza98798798
cliente = cliente_ayumi_souza98798798

# (veiculo)
from entrada_de_dados.lista_de_carros_registrados import carro_toyota_corolla_818630
carro = carro_toyota_corolla_818630

valor_negociado = "51000"

venda_596013 = Venda(data, codigo, loja, cliente, carro, valor_negociado)


add_venda_na_lista_do_main(venda_596013)

# -------------------------------------------------------


