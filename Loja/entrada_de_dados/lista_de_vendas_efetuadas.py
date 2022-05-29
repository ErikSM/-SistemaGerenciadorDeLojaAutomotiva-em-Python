from estrutura.Venda import Venda

vendas_registradas = list()


def add_venda_na_lista_do_main(venda: Venda):
    vendas_registradas.append(venda)


#  --------------  -----------   --------------   ------------- -----


from relatorios_de_venda.venda_codigo_765018 import venda_765018
add_venda_na_lista_do_main(venda_765018)


from relatorios_de_venda.venda_codigo_590404 import venda_590404
add_venda_na_lista_do_main(venda_590404)


from relatorios_de_venda.venda_codigo_209604 import venda_209604
add_venda_na_lista_do_main(venda_209604)


from relatorios_de_venda.venda_codigo_901301 import venda_901301
add_venda_na_lista_do_main(venda_901301)


from relatorios_de_venda.venda_codigo_53575 import venda_53575
add_venda_na_lista_do_main(venda_53575)


from relatorios_de_venda.venda_codigo_614330 import venda_614330
add_venda_na_lista_do_main(venda_614330)

