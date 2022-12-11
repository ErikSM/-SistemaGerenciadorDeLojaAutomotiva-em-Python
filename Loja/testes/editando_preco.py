def mascara_preco(numero):
    flutuante = float(numero)
    string = f'{flutuante:.2f}'
    referencia = _encontrar_posicao_do_caractere(string, ".")

    parte_um = string[:referencia]
    parte_dois = string[referencia + 1:]

    return 'R$:{},{}'.format(parte_um, parte_dois)


def _encontrar_posicao_do_caractere(string, caractere):
    indice = 0
    while indice < len(string):
        if string[indice] == caractere:
            return indice
        indice = indice + 1

    return -1


print(mascara_preco("235a399"))
