from estrutura.Carro import Carro

carros_registrados = list()
codigos_de_carros_existentes = list()


def add_carro_na_lista(carro: Carro, variavel, cnpj_loja_vinculada, linha_no_arquivo):
    carro.nome_da_variavel = str(variavel)
    carro.cnpj_loja = cnpj_loja_vinculada
    carro.linha_no_arquivo = linha_no_arquivo
    carros_registrados.append(carro)
    _atualizar_contador_da_lista()
    _add_novo_codigo_na_lista_de_codigos_ja_existentes(carro.codigo)


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in carros_registrados:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo):
    codigo_int = int(codigo)
    codigos_de_carros_existentes.append(codigo_int)


def _remover_codigo_da_lista_de_codigos_existentes(codigo):
    codigos_de_carros_existentes.remove(int(codigo))


def remover_carro_da_lista(carro: Carro, codigo):
    carros_registrados.remove(carro)
    carro.codigo_de_venda = str(codigo)
    _remover_codigo_da_lista_de_codigos_existentes(carro.codigo)
    _atualizar_contador_da_lista()


# --------------------  -----------------   ------------   ------------   ----


montadora = "WolksWagon"
nome = "Gol"
ano = "2020"
valor_de_aquisicao = "45000"
codigo_de_registro = "988526"
carro_988526 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_988526, "carro_988526", 124134100000, 43)


montadora = "Toyota"
nome = "Corolla"
ano = "2015"
valor_de_aquisicao = "50000"
codigo_de_registro = "78502"
carro_78502 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_78502, "carro_78502", 124134100000, 52)


montadora = "Wolkswagen"
nome = "Golf"
ano = "2012"
valor_de_aquisicao = "27000"
codigo_de_registro = "942353"
carro_942353 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_942353, "carro_942353", 124134100000, 61)


montadora = "Toyota"
nome = "hilux"
ano = "2021"
valor_de_aquisicao = "300000"
codigo_de_registro = "679209"
carro_679209 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_679209, "carro_679209", 124134100000, 70)


montadora = "WolksWagen"
nome = "Gol"
ano = "2020"
valor_de_aquisicao = "50000"
codigo_de_registro = "827583"
carro_827583 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_827583, "carro_827583", 124134100000, 79)


montadora = "Toyota "
nome = "Corolla"
ano = "2019"
valor_de_aquisicao = "60000"
codigo_de_registro = "873311"
carro_873311 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_873311, "carro_873311", 124134100000, 88)


montadora = "WolksWagen"
nome = "Gol"
ano = "2013"
valor_de_aquisicao = "12000"
codigo_de_registro = "492654"
carro_492654 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_492654, "carro_492654", 124134100000, 97)


montadora = "Nissan"
nome = "Fairlady Z"
ano = "2020"
valor_de_aquisicao = "120000"
codigo_de_registro = "719373"
carro_719373 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_719373, "carro_719373", 124134100000, 106)


remover_carro_da_lista(carro_873311, "384399")


remover_carro_da_lista(carro_988526, "387595")

