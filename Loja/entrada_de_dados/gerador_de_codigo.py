from random import sample
from entrada_de_dados.lista_de_vendas_efetuadas import codigos_de_vendas_existentes


def criar_codigo_unico_de_venda():
    codigo = _gerador_de_codigo_aleatorio()
    variavel = True

    while variavel:
        if codigo in codigos_de_vendas_existentes:
            codigo = _gerador_de_codigo_aleatorio()
        if codigo not in codigos_de_vendas_existentes:
            variavel = False

    return codigo


def _gerador_de_codigo_aleatorio():
    codigo_em_lista = sample(range(0, 1000000), 1)
    codigo_gerado = codigo_em_lista[0]

    return codigo_gerado
