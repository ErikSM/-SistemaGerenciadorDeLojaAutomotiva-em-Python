from random import sample

lista = [0, 2, 4, 6, 8, 10]


def elaborar_criar_codigo_unico():

    codigo = _elaborar_gerador_de_codigo()
    variavel = True

    while variavel:
        if codigo in lista:
            print(f"repetido: {codigo}")
            codigo = _elaborar_gerador_de_codigo()

        elif codigo not in lista:
            print(f"\nOK: {codigo}")
            variavel = False

    return codigo


def _elaborar_gerador_de_codigo():

    codigo_em_lista = sample(range(0, 10), 1)
    codigo_gerado = codigo_em_lista[0]

    return codigo_gerado


teste = elaborar_criar_codigo_unico()
print(teste)
