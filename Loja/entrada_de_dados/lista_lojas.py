from estrutura.Loja import Loja


lojas_registradas = list()
codigos_de_lojas_existentes = list()


def add_loja_na_lista(loja: Loja):
    loja.nome_da_variavel = f"loja_{loja.codigo}"
    lojas_registradas.append(loja)

    _atualizar_contador_da_lista()
    _add_novo_codigo_na_lista_de_codigos_ja_existentes(loja.codigo)


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0

    for i in lojas_registradas:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo_novo):
    codigo_int = int(codigo_novo)
    codigos_de_lojas_existentes.append(codigo_int)


def remover_loja_da_lista(loja):
    lojas_registradas.remove(loja)
    codigos_de_lojas_existentes.remove(int(loja.codigo))
    _atualizar_contador_da_lista()


# ------------------ ---------------------- -------------------- -------


nome = "Test Store"
cnpj = "43217051000182"
telefone = "059988134342"
email = "test_store@gmail.com"
codigo = "378796"
loja_378796 = Loja(nome, cnpj, telefone, email, codigo)
add_loja_na_lista(loja_378796)

nome = "Secound Test Store"
cnpj = "83037728000115"
telefone = "059988543421"
email = "secound_test_store@hotmail.com"
codigo = "157518"
loja_157518 = Loja(nome, cnpj, telefone, email, codigo)
add_loja_na_lista(loja_157518)
