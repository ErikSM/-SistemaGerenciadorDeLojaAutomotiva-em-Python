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

