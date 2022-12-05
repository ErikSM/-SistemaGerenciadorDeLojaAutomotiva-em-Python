from estrutura.Loja import Loja

lojas_registradas = list()


def add_loja_na_lista(loja: Loja, variavel):
    loja.nome_da_variavel = variavel
    lojas_registradas.append(loja)
    _atualizar_contador_da_lista()


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in lojas_registradas:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


def remover_loja_da_lista(loja):
    lojas_registradas.remove(loja)
    _atualizar_contador_da_lista()


# ------------------ ---------------------- -------------------- -------


nome = "Test Store"
cnpj = "124134100000"
telefone = "99881343425"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista(loja_test_store, "loja_test_store")


nome = "Secound Test Store"
cnpj = "1234990876543"
telefone = "987655889099"
loja_secound_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista(loja_secound_test_store, "loja_secound_test_store")

remover_loja_da_lista(loja_secound_test_store)


nome = "Secound Test Store"
cnpj = "8769990600000"
telefone = "990088765432"
loja_secound_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista(loja_secound_test_store, "loja_secound_test_store")



nome = "Test Store 3"
cnpj = "24987298472987"
telefone = "987986789776987"
loja_test_store_3 = Loja(nome, cnpj, telefone)
add_loja_na_lista(loja_test_store_3, "loja_test_store_3")



remover_loja_da_lista(loja_test_store_3)

