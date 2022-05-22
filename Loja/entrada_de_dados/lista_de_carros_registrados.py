from estrutura.Carro import Carro


carros_registrados = list()

variavel_contador_de_posicao_na_lista = 0


def add_carro_na_lista_do_main(carro: Carro, posicao):
    carro.posicao_na_lista = posicao
    carros_registrados.append(carro)

# --------------------  -----------------   ------------   ------------   ----

montadora = "Toyota"
nome = "Prius"
ano = "22"
preco = "1000000"
carro_Toyota_Prius = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_Toyota_Prius, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


montadora = "Nissan"
nome = "Skyline"
ano = "19"
preco = "900000"
carro_Nissan_Skyline = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_Nissan_Skyline, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


montadora = "Subaru"
nome = "WRX"
ano = "15"
preco = "500000"
carro_Subaru_WRX = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_Subaru_WRX, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1



montadora = "Wolks Wagen"
nome = "Golf"
ano = "25"
preco = "2000000"
carro_Wolks_Wagen_Golf = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_Wolks_Wagen_Golf, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


montadora = "Toyota"
nome = "Alphard"
ano = "22"
preco = "300000"
carro_Toyota_Alphard = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_Toyota_Alphard, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


montadora = "Ferrari"
nome = "FerrariX"
ano = "26"
preco = "4000000"
carro_Ferrari_FerrariX = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_Ferrari_FerrariX, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


montadora = "Toyota"
nome = "MarkII100"
ano = "12"
preco = "500000"
carro_Toyota_MarkII100 = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_Toyota_MarkII100, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


montadora = "WolksWagen"
nome = "Fuska"
ano = "2"
preco = "50 000"
carro_wolkswagen_fuska = Carro(montadora, nome, ano, preco)
add_carro_na_lista_do_main(carro_wolkswagen_fuska, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

