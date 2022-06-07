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


montadora = "Mazda"
nome = "RX7"
ano = "2003"
preco = "150 000"
carro_mazda_rx7_765597 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_mazda_rx7_765597, "carro_mazda_rx7_765597")
_atualizar_contador_da_lista()


montadora = "Ford"
nome = "Fusion"
ano = "2010"
preco = "90 000"
carro_ford_fusion_629286 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_ford_fusion_629286, "carro_ford_fusion_629286")
_atualizar_contador_da_lista()


montadora = "Toyota"
nome = "Prius"
ano = "2007"
preco = "320 000"
carro_toyota_prius_774811 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_prius_774811, "carro_toyota_prius_774811")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_toyota_prius_774811, "698138")


remover_carro_da_lista(carro_mazda_rx7_765597, "541416")


montadora = "Toyota"
nome = "Lexus G35"
ano = "2009"
preco = "85 000"
carro_toyota_lexus_g35_295474 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_lexus_g35_295474, "carro_toyota_lexus_g35_295474")
_atualizar_contador_da_lista()


montadora = "Fiat"
nome = "Uno"
ano = "2015"
preco = "30 000"
carro_fiat_uno_75705 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_fiat_uno_75705, "carro_fiat_uno_75705")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_fiat_uno_75705, "268077")


montadora = "Toyota"
nome = "Prius"
ano = "2022"
preco = "100 000"
carro_toyota_prius_1811 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_toyota_prius_1811, "carro_toyota_prius_1811")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_toyota_prius_1811, "794678")


montadora = "Fiat"
nome = "Uno"
ano = "2022"
preco = "45 000"
carro_fiat_uno_942082 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_fiat_uno_942082, "carro_fiat_uno_942082")
_atualizar_contador_da_lista()


remover_carro_da_lista(carro_fiat_uno_942082, "559874")

