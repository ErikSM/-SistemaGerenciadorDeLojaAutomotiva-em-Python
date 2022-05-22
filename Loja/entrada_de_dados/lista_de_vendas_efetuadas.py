from estrutura.Venda import Venda

vendas_registradas = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


#  --------------  -----------   --------------   ------------- -----


from relatorios_de_venda.venda_codigo_67103 import venda_67103
add_venda_na_lista_do_main(venda_67103)


from relatorios_de_venda.venda_codigo_294497 import venda_294497
add_venda_na_lista_do_main(venda_294497)


from relatorios_de_venda.venda_codigo_943684 import venda_943684
add_venda_na_lista_do_main(venda_943684)


from relatorios_de_venda.venda_codigo_249414 import venda_249414
add_venda_na_lista_do_main(venda_249414)

