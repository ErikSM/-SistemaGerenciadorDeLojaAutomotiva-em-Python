from estrutura.Carro import Carro

carros_registrados = list()


def add_carro_na_lista_do_main(carro: Carro, variavel):
    carro.nome_da_variavel = str(variavel)
    carros_registrados.append(carro)
    _atualizar_contador_da_lista()


def remover_carro_da_lista(carro: Carro, codigo):
    carros_registrados.remove(carro)
    carro.codigo_de_venda = str(codigo)
    _atualizar_contador_da_lista()


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in carros_registrados:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


# --------------------  -----------------   ------------   ------------   ----


montadora = "Toyota"
nome = "Prius"
ano = "2015"
preco = "100 000"
carro_toyota_prius_55076 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_prius_55076, "carro_toyota_prius_55076")
_atualizar_contador_da_lista()


montadora = "WolksWagen"
nome = "Golf GTI"
ano = "2009"
preco = "20 000"
carro_wolkswagen_golf_gti_570752 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_wolkswagen_golf_gti_570752, "carro_wolkswagen_golf_gti_570752")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_wolkswagen_golf_gti_570752, "155920")


montadora = "Fiat"
nome = "Uno"
ano = "2002"
preco = "12 000"
carro_fiat_uno_561718 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_fiat_uno_561718, "carro_fiat_uno_561718")
_atualizar_contador_da_lista()


montadora = "Toyota"
nome = "Lexus"
ano = "2008"
preco = "70 000"
carro_toyota_lexus_856048 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_lexus_856048, "carro_toyota_lexus_856048")
_atualizar_contador_da_lista()


montadora = "Nissan"
nome = "GTR 35"
ano = "2015"
preco = "170 000"
carro_nissan_gtr_35_494875 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_nissan_gtr_35_494875, "carro_nissan_gtr_35_494875")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_fiat_uno_561718, "6084")


remover_carro_da_lista(carro_toyota_lexus_856048, "393755")


montadora = "Toyota"
nome = "Hilux"
ano = "2016"
preco = "200 000"
carro_toyota_hilux_371922 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_hilux_371922, "carro_toyota_hilux_371922")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_toyota_hilux_371922, "907758")


remover_carro_da_lista(carro_toyota_prius_55076, "687154")

