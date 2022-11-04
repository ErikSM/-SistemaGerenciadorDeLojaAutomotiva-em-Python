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
nome = "Corolla"
ano = "2009"
preco = "40000"
carro_toyota_corolla_818630 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_corolla_818630, "carro_toyota_corolla_818630")
_atualizar_contador_da_lista()


montadora = "WolksWagen"
nome = "Gol"
ano = "2015"
preco = "20000"
carro_wolkswagen_gol_875414 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_wolkswagen_gol_875414, "carro_wolkswagen_gol_875414")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_wolkswagen_gol_875414, "124776")


remover_carro_da_lista(carro_toyota_corolla_818630, "596013")


montadora = "WolksWagen"
nome = "Golf"
ano = "2010"
preco = "15000"
carro_wolkswagen_golf_520954 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_wolkswagen_golf_520954, "carro_wolkswagen_golf_520954")
_atualizar_contador_da_lista()

