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
preco = "70 000"
carro_toyota_prius_533530 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_prius_533530, "carro_toyota_prius_533530")
_atualizar_contador_da_lista()


montadora = "Ferrari"
nome = "Ferrari GP X"
ano = "2013"
preco = "500 000"
carro_ferrari_ferrari_gp_x_459192 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_ferrari_ferrari_gp_x_459192, "carro_ferrari_ferrari_gp_x_459192")
_atualizar_contador_da_lista()


montadora = "Nissan"
nome = "Skyline 35"
ano = "2007"
preco = "300 000"
carro_nissan_skyline_35_31825 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_nissan_skyline_35_31825, "carro_nissan_skyline_35_31825")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_toyota_prius_533530, 765018)


remover_carro_da_lista(carro_ferrari_ferrari_gp_x_459192, 590404)


montadora = "WolksWagen"
nome = "Golf"
ano = "2013"
preco = "60 000"
carro_wolkswagen_golf_846557 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_wolkswagen_golf_846557, "carro_wolkswagen_golf_846557")
_atualizar_contador_da_lista()


montadora = "Mazda"
nome = "RX7"
ano = "2003"
preco = "150 000"
carro_mazda_rx7_765597 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_mazda_rx7_765597, "carro_mazda_rx7_765597")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_nissan_skyline_35_31825, 209604)


montadora = "Ford"
nome = "Fusion"
ano = "2010"
preco = "90 000"
carro_ford_fusion_629286 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_ford_fusion_629286, "carro_ford_fusion_629286")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_wolkswagen_golf_846557, 901301)


montadora = "Wolkswagen"
nome = "Polo"
ano = "2007"
preco = "40 000"
carro_wolkswagen_polo_603321 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_wolkswagen_polo_603321, "carro_wolkswagen_polo_603321")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_ford_fusion_629286, 53575)


montadora = "WolksWagen"
nome = "Hilux"
ano = "2010"
preco = "200 000"
carro_wolkswagen_hilux_916235 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_wolkswagen_hilux_916235, "carro_wolkswagen_hilux_916235")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_wolkswagen_hilux_916235, 614330)

