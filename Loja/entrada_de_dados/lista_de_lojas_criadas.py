from estrutura.Loja import Loja

lojas_registradas = list()

variavel_contador_de_posicao_na_lista = 0

def add_loja_na_lista_do_main (loja: Loja, posicao):
    loja.posicao_na_lista = posicao
    lojas_registradas.append(loja)

# ----------  ---------------   ---------------   ---------------------

nome = "Test Store"
cnpj = "2422"
telefone = "2342"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Secound Test Store"
cnpj = "678678"
telefone = "678678"
loja_secound_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_secound_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "New Test Store"
cnpj = "234234"
telefone = "053 575"
loja_new_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_new_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Quarta Test Store"
cnpj = "245252"
telefone = "053 453453"
loja_quarta_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_quarta_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Five Test Store"
cnpj = "242525"
telefone = "053 9868768"
loja_five_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_five_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Six Test Store"
cnpj = "34509809"
telefone = "053 87987"
loja_six_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_six_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Setima Test Store"
cnpj = "4525"
telefone = "053 9872242"
loja_setima_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_setima_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Hachi Test Store"
cnpj = "098097"
telefone = "053 2342"
loja_hachi_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_hachi_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Venus Test Store"
cnpj = "32425"
telefone = "054876876876"
loja_venus_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_venus_test_store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Mars Test Store"
cnpj = "23432342342"
telefone = "054234234234"
loja_Mars_Test_Store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_Mars_Test_Store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Sun Test Store"
cnpj = "876876"
telefone = "05476765765"
loja_Sun_Test_Store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_Sun_Test_Store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Super Store Test"
cnpj = "876786"
telefone = "7657657"
loja_Super_Store_Test = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_Super_Store_Test, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "Mega Test Store"
cnpj = "234234"
telefone = "32424323"
loja_Mega_Test_Store = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_Mega_Test_Store, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1


nome = "New TEst"
cnpj = "2342"
telefone = "341"
loja_new_test = Loja(nome, cnpj, telefone)
add_loja_na_lista_do_main(loja_new_test, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1
