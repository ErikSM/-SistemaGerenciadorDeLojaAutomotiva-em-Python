from estrutura.Loja import Loja

lojas_registradas = list()

variavel_contador_de_posicao_na_lista = 0


def add_loja_na_lista_do_main(loja: Loja, posicao):
    loja.posicao_na_lista = posicao
    lojas_registradas.append(loja)


nome = "Test Store"
cnpj = "675"
telefone = "76565465"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Secound Test Store"
cnpj = "4254"
telefone = "987987"
loja_secound_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_secound_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Store Test 3"
cnpj = "324"
telefone = "4525"
loja_store_test_3 = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_store_test_3, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Four Store Test"
cnpj = "2552"
telefone = "435252"
loja_four_store_test = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_four_store_test, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

