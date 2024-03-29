from estrutura.Carro import Carro

carros_registrados = list()
codigos_de_carros_existentes = list()


def add_carro_na_lista(carro: Carro, cnpj_loja_vinculada, linha_no_arquivo):
    carro.cnpj_loja = cnpj_loja_vinculada
    carro.linha_no_arquivo = linha_no_arquivo
    carro.nome_da_variavel = f"carro_{carro.codigo}"
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


def remover_carro_da_lista(carro: Carro, codigo):
    carros_registrados.remove(carro)
    carro.codigo_de_venda = str(codigo)

    _remover_codigo_da_lista_de_codigos_existentes(carro.codigo)
    _atualizar_contador_da_lista()


def _remover_codigo_da_lista_de_codigos_existentes(codigo):
    codigos_de_carros_existentes.remove(int(codigo))


# --------------------  -----------------   ------------   ------------   ----


montadora = "WolksWagon"
nome = "Gol"
ano = "2020"
valor_de_aquisicao = "45000"
codigo_de_registro = "988526"
carro_988526 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_988526, 43217051000182, 47)


montadora = "Toyota"
nome = "Corolla"
ano = "2015"
valor_de_aquisicao = "50000"
codigo_de_registro = "78502"
carro_78502 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_78502, 43217051000182, 56)


montadora = "Wolkswagen"
nome = "Golf"
ano = "2012"
valor_de_aquisicao = "27000"
codigo_de_registro = "942353"
carro_942353 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_942353, 43217051000182, 65)


montadora = "Toyota"
nome = "hilux"
ano = "2021"
valor_de_aquisicao = "300000"
codigo_de_registro = "679209"
carro_679209 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_679209, 43217051000182, 74)


montadora = "WolksWagen"
nome = "Gol"
ano = "2020"
valor_de_aquisicao = "50000"
codigo_de_registro = "827583"
carro_827583 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_827583, 43217051000182, 83)


montadora = "Toyota "
nome = "Corolla"
ano = "2019"
valor_de_aquisicao = "60000"
codigo_de_registro = "873311"
carro_873311 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_873311, 43217051000182, 92)


montadora = "WolksWagen"
nome = "Gol"
ano = "2013"
valor_de_aquisicao = "12000"
codigo_de_registro = "492654"
carro_492654 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_492654, 43217051000182, 101)


montadora = "Nissan"
nome = "Fairlady Z"
ano = "2020"
valor_de_aquisicao = "120000"
codigo_de_registro = "719373"
carro_719373 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_719373, 43217051000182, 110)


remover_carro_da_lista(carro_873311, "384399")


remover_carro_da_lista(carro_988526, "387595")


remover_carro_da_lista(carro_719373, "678358")


remover_carro_da_lista(carro_827583, "33373")


remover_carro_da_lista(carro_492654, "40082")


remover_carro_da_lista(carro_78502, "92254")


remover_carro_da_lista(carro_942353, "693294")


montadora = "Wolkswagen"    
nome = "Gol"    
ano = "2019"    
valor_de_aquisicao = "30000"    
codigo_de_registro = "561458"    
carro_561458 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_561458, 43217051000182, 140)


remover_carro_da_lista(carro_561458, "375453")


montadora = "Fiat"    
nome = "Uno"    
ano = "2019"    
valor_de_aquisicao = "30000"    
codigo_de_registro = "525054"    
carro_525054 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_525054, 43217051000182, 152)


montadora = "Wolkswagen"    
nome = "Golf"    
ano = "2019"    
valor_de_aquisicao = "50000"    
codigo_de_registro = "805403"    
carro_805403 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_805403, 43217051000182, 161)


remover_carro_da_lista(carro_525054, "953711")

