from estrutura.Loja import Loja

lojas_registradas = list()

variavel_contador_de_posicao_na_lista = 0


def add_loja_na_lista_do_main(loja: Loja, posicao, variavel):
    loja.posicao_na_lista = posicao
    loja.nome_da_variavel = variavel
    lojas_registradas.append(loja)


nome = "Test Store"
cnpj = "675"
telefone = "76565465"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store, variavel_contador_de_posicao_na_lista, "loja_test_store")
variavel_contador_de_posicao_na_lista += 1


nome = "Secound Test Store"
cnpj = "4254"
telefone = "987987"
loja_secound_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_secound_test_store, variavel_contador_de_posicao_na_lista, "loja_secound_test_store")
variavel_contador_de_posicao_na_lista += 1



nome = "Test Store 3"
cnpj = "2342342"
telefone = "9080980"
loja_test_store_3 = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store_3, variavel_contador_de_posicao_na_lista, "loja_test_store_3")
variavel_contador_de_posicao_na_lista += 1

