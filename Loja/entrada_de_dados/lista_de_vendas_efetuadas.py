from estrutura.Venda import Venda

vendas_registradas = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


#  --------------  -----------   --------------   ------------- -----


from relatorios_de_venda.venda_codigo_99863 import venda_99863
add_venda_na_lista_do_main(venda_99863)


from relatorios_de_venda.venda_codigo_912296 import venda_912296
add_venda_na_lista_do_main(venda_912296)


from relatorios_de_venda.venda_codigo_109880 import venda_109880
add_venda_na_lista_do_main(venda_109880)


from relatorios_de_venda.venda_codigo_112245 import venda_112245
add_venda_na_lista_do_main(venda_112245)


from relatorios_de_venda.venda_codigo_255173 import venda_255173
add_venda_na_lista_do_main(venda_255173)

