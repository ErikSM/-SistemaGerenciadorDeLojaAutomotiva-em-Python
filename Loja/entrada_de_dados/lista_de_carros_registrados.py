from estrutura.Carro import Carro

carros_registrados = list()


def add_carro_na_lista_do_main(carro: Carro, variavel):
    carro.nome_da_variavel = str(variavel)
    carros_registrados.append(carro)
    _atualizar_contador_da_lista()


def remover_carro_da_lista(carro: Carro):
    carros_registrados.remove(carro)
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

