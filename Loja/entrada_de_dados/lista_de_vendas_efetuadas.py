from estrutura.Venda import Venda

vendas_registradas = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


#  --------------  -----------   --------------   ------------- -----


from relatorios_de_venda.venda_codigo_974793 import venda_974793
add_venda_na_lista_do_main(venda_974793)


from relatorios_de_venda.venda_codigo_875655 import venda_875655
add_venda_na_lista_do_main(venda_875655)


from relatorios_de_venda.venda_codigo_585864 import venda_585864
add_venda_na_lista_do_main(venda_585864)

