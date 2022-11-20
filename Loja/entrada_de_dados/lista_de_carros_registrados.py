from estrutura.Carro import Carro

carros_registrados = list()

codigos_de_carros_existentes = list()


def add_carro_na_lista_do_main(carro: Carro, variavel):
    carro.nome_da_variavel = str(variavel)
    carros_registrados.append(carro)
    _add_novo_codigo_na_lista_de_codigos_ja_existentes(carro.codigo)
    _atualizar_contador_da_lista()


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo):
    codigo_int = int(codigo)
    codigos_de_carros_existentes.append(codigo_int)


def remover_carro_da_lista(carro: Carro, codigo):
    carros_registrados.remove(carro)
    carro.codigo_de_venda = str(codigo)
    _remover_codigo_da_lista_de_codigos_existentes(carro.codigo)
    _atualizar_contador_da_lista()


def _remover_codigo_da_lista_de_codigos_existentes(codigo):
    codigos_de_carros_existentes.remove(int(codigo))


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in carros_registrados:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


# --------------------  -----------------   ------------   ------------   ----


montadora = "WolksWagen"
nome = "Gol"
ano = "2012"
preco = "18000"
codigo = "339991"
carro_wolkswagen_gol_339991 = Carro(montadora, nome, ano, preco, codigo)
add_carro_na_lista_do_main(carro_wolkswagen_gol_339991, "carro_wolkswagen_gol_339991")


montadora = "Toyota"
nome = "Corolla"
ano = "2014"
preco = "23000"
codigo = "754655"
carro_toyota_corolla_754655 = Carro(montadora, nome, ano, preco, codigo)
add_carro_na_lista_do_main(carro_toyota_corolla_754655, "carro_toyota_corolla_754655")


montadora = "Toyota"
nome = "Hilux"
ano = "2018"
preco = "180000"
codigo = "377261"
carro_toyota_hilux_377261 = Carro(montadora, nome, ano, preco, codigo)
add_carro_na_lista_do_main(carro_toyota_hilux_377261, "carro_toyota_hilux_377261")


remover_carro_da_lista(carro_wolkswagen_gol_339991, "115167")


remover_carro_da_lista(carro_toyota_hilux_377261, "27637")


montadora = "WolksWagen"
nome = "Polo"
ano = "2008"
preco = "15000"
codigo = "293417"
carro_wolkswagen_polo_293417 = Carro(montadora, nome, ano, preco, codigo)
add_carro_na_lista_do_main(carro_wolkswagen_polo_293417, "carro_wolkswagen_polo_293417")

remover_carro_da_lista(carro_toyota_corolla_754655, "367251")


montadora = "Toyota"
nome = "Prius"
ano = "2018"
valor_de_aquisicao = "80000"
codigo_de_registro = "743358"
carro_toyota_prius_743358 = Carro(montadora, nome, ano, preco, codigo)
add_carro_na_lista_do_main(carro_toyota_prius_743358, "carro_toyota_prius_743358")

