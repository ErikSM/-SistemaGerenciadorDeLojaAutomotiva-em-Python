
class Email:

    def __init__(self, endereco):

        self.email = endereco

        self.email_valido = bool()

        self.msg_erro = str()
        self.operadoras_aceitas = list()
        self.finais_aceitos = list()
        self.caracteres: tuple

    def __str__(self):
        self._tirar_espacos_string()

        return self.email

    def validar(self):

        erro_formato = "ErRor(Endereco Invalido)"
        erro_operadora = "ErRor(Operadora Invalida)"
        erro_final = "ErRor(Final Invalido)"

        self.operadoras_aceitas.append("hotmail")
        self.operadoras_aceitas.append("gmail")
        self.operadoras_aceitas.append("yahoo")
        self.operadoras_aceitas.append("outlook")

        self.finais_aceitos.append("com")
        self.finais_aceitos.append("com.br")

        if " " in self.email:
            self.msg_erro = erro_formato
            self.email_valido = False

        elif "@" in self.email and "." in self.email:
            self._encontrar_posicao_do_caractere()

            referencia_um = self.caracteres[0]
            referencia_dois = self.caracteres[1]

            operadora = self.email[referencia_um + 1: referencia_dois]
            final = self.email[referencia_dois + 1:]

            if operadora in self.operadoras_aceitas:
                if final in self.finais_aceitos:
                    self.email_valido = True
                else:
                    self.msg_erro = erro_final
                    self.email_valido = False
            else:
                self.msg_erro = erro_operadora
                self.email_valido = False

        else:
            self.msg_erro = erro_formato
            self.email_valido = False

        return self.email_valido

    def _tirar_espacos_string(self):
        string_espalhado = self.email.split()

        string_sem_espaco = "".join(string_espalhado)
        string_sem_letra_maiuscula = string_sem_espaco.lower()

        self.email = string_sem_letra_maiuscula

    def _encontrar_posicao_do_caractere(self):

        caracteres = ("@", ".")
        lista = list()

        for i in caracteres:
            indice = 0
            while indice < len(self.email):
                if self.email[indice] == i:
                    lista.append(indice)
                indice += 1

        self.caracteres = (lista[0], lista[1])


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
