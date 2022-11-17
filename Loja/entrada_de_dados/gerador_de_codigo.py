from random import sample


def criar_codigo_unico(lista):
    codigo = _gerador_de_codigo_aleatorio()
    variavel = True

    while variavel:
        if codigo in lista:
            codigo = _gerador_de_codigo_aleatorio()
        if codigo not in lista:
            variavel = False

    return codigo


def _gerador_de_codigo_aleatorio():
    codigo_em_lista = sample(range(0, 1000000), 1)
    codigo_gerado = codigo_em_lista[0]

    return codigo_gerado
