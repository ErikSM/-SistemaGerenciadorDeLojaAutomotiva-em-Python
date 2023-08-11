from random import sample


def criar_codigo_unico(lista_de_codigos):

    codigo = _gerador_de_codigo_aleatorio()
    criando_codigo = True

    while criando_codigo:
        if codigo in lista_de_codigos:
            codigo = _gerador_de_codigo_aleatorio()
        if codigo not in lista_de_codigos:
            criando_codigo = False

    return codigo


def _gerador_de_codigo_aleatorio():

    codigo_em_lista = sample(range(0, 1000000), 1)
    codigo_gerado = codigo_em_lista[0]

    return codigo_gerado
