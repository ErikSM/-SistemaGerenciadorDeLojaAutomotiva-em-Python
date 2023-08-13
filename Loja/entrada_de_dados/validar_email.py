

def checar_email(string):
    operadoras_aceitas = list()
    operadoras_aceitas.append("hotmail")
    operadoras_aceitas.append("gmail")
    operadoras_aceitas.append("yahoo")
    operadoras_aceitas.append("outlook")

    finais_aceitos = list()
    finais_aceitos.append("com")
    finais_aceitos.append("com.br")

    string_editada = _tirar_espacos_da_string(string)

    mensagem_de_erro_de_formato = "erro_formato"

    mensagem_de_erro_de_operadora = "erro_operadora"

    mensagem_de_erro_de_final = "erro_final"

    if "@" in string_editada and "." in string_editada:
        referencia_um = _encontrar_posicao_do_caractere(string_editada, "@")
        referencia_dois = _encontrar_posicao_do_caractere(string_editada, ".")

        operadora = string_editada[referencia_um + 1: referencia_dois]
        final = string_editada[referencia_dois + 1:]

        if operadora in operadoras_aceitas:
            if final in finais_aceitos:
                return string_editada
            else:
                return mensagem_de_erro_de_final
        else:
            return mensagem_de_erro_de_operadora
    else:
        return mensagem_de_erro_de_formato


def _tirar_espacos_da_string(string):
    string_espalhado = string.split()
    string_sem_espaco = "".join(string_espalhado)
    string_sem_letra_maiuscula = string_sem_espaco.lower()

    string_apos_teste = string_sem_letra_maiuscula
    return string_apos_teste


def _encontrar_posicao_do_caractere(string, caractere):
    indice = 0
    while indice < len(string):
        if string[indice] == caractere:
            return indice
        indice = indice + 1

    return -1
