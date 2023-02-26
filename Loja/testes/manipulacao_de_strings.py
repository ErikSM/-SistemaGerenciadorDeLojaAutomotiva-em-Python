

def _tirar_espacos_de_string(string):
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


def validar_email(string):
    operadoras_aceitas = list()
    operadoras_aceitas.append("hotmail")
    operadoras_aceitas.append("gmail")
    operadoras_aceitas.append("yahoo")
    operadoras_aceitas.append("outlook")

    finais_aceitos = list()
    finais_aceitos.append("com")
    finais_aceitos.append("com.br")

    string_editada = _tirar_espacos_de_string(string)

    mensagem_de_erro_de_formato = "ErRor(Endereco Invalido)\n-> " \
                                  "verifique se digitou corretamente"

    mensagem_de_erro_de_operadora = "ErRor(Operadora Invalida)\n" \
                                    "Aceitas: -yahoo, -hotmail/outlook ou -gmail"

    mensagem_de_erro_de_final = "ErRor(Endereco Invalido)"

    if "@" in string_editada and "." in string_editada:
        referencia_um = _encontrar_posicao_do_caractere(string_editada, "@")
        referencia_dois = _encontrar_posicao_do_caractere(string_editada, ".")

        operadora = string_editada[referencia_um + 1: referencia_dois]
        final = string_editada[referencia_dois + 1:]

        if operadora in operadoras_aceitas:
            if final in finais_aceitos:
                print(string_editada)
            else:
                print(mensagem_de_erro_de_final)
        else:
            print(mensagem_de_erro_de_operadora)
    else:
        print(mensagem_de_erro_de_formato)


string_para_testar = " Erik  @yahoo . c   om.br"

validar_email(string_para_testar)
