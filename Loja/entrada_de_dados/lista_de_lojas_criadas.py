from estrutura.Loja import Loja

lojas_registradas = list()

variavel_contador_de_posicao_na_lista = 0


def add_loja_na_lista_do_main(loja: Loja, posicao):
    loja.posicao_na_lista = posicao
    lojas_registradas.append(loja)


nome = "haha"
cnpj = "sjfaoj"
telefone = "23424"
loja_haha = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_haha, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


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


nome = "Store Four Test"
cnpj = "32424"
telefone = "3421"
loja_store_four_test = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_store_four_test, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Five Test Store"
cnpj = "2341"
telefone = "3414"
loja_five_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_five_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

