from estrutura.Carro import Carro

carros_registrados = list()

codigos_de_carros_existentes = list()


def add_carro_na_lista(carro: Carro, variavel, cnpj_loja_vinculada):
    carro.nome_da_variavel = str(variavel)
    carro.cnpj_loja = cnpj_loja_vinculada
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
carro_wolkswagon_gol_988526 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_wolkswagon_gol_988526, "carro_wolkswagon_gol_988526", 124134100000)

montadora = "Toyota"
nome = "Corolla"
ano = "2015"
valor_de_aquisicao = "50000"
codigo_de_registro = "78502"
carro_toyota_corolla_78502 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_toyota_corolla_78502, "carro_toyota_corolla_78502", 124134100000)

montadora = "Wolkswagen"
nome = "Golf"
ano = "2012"
valor_de_aquisicao = "27000"
codigo_de_registro = "942353"
carro_wolkswagen_golf_942353 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_wolkswagen_golf_942353, "carro_wolkswagen_golf_942353", 124134100000)


montadora = "Toyota"    
nome = "hilux"    
ano = "2021"    
valor_de_aquisicao = "300000"    
codigo_de_registro = "679209"    
carro_toyota_hilux_679209 = Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)
add_carro_na_lista(carro_toyota_hilux_679209, "carro_toyota_hilux_679209", 124134100000)


remover_carro_da_lista(carro_toyota_corolla_78502, "120550")
