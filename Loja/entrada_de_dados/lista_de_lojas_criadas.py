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
cnpj = "2423794"
telefone = "0977687"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store, "loja_test_store")
_atualizar_contador_da_lista()


remover_loja_da_lista(loja_test_store)


nome = "Test Store"
cnpj = "234242352"
telefone = "090786757"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store, "loja_test_store")
_atualizar_contador_da_lista()


loja_test_store.senha = "1234"


loja_test_store.senha = ""


loja_test_store.senha = ""


loja_test_store.senha = "1234"


loja_test_store.senha = "None"


loja_test_store.senha = None

