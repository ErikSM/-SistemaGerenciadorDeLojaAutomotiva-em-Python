from estrutura.Loja import Loja

lojas_registradas = list()


def add_loja_na_lista_do_main(loja: Loja, variavel):
    loja.nome_da_variavel = variavel
    lojas_registradas.append(loja)


def remover_loja_da_lista(loja):
    lojas_registradas.remove(loja)
    _atualizar_contador_da_lista()


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in lojas_registradas:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


# ------------------ ---------------------- -------------------- -------

nome = "Test Store"
cnpj = "675"
telefone = "76565465"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store, "loja_test_store")
_atualizar_contador_da_lista()


nome = "Secound Test Store"
cnpj = "4254"
telefone = "987987"
loja_secound_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_secound_test_store, "loja_secound_test_store")
_atualizar_contador_da_lista()


nome = "Test Store 3"
cnpj = "2342342"
telefone = "9080980"
loja_test_store_3 = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store_3, "loja_test_store_3")
_atualizar_contador_da_lista()


nome = "Four Test Store"
cnpj = "9879872423"
telefone = "76576000"
loja_four_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_four_test_store, "loja_four_test_store")
_atualizar_contador_da_lista()


remover_loja_da_lista(loja_four_test_store)

