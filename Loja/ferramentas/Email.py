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

        erro_caracter = "ErRor(Caracter Proibido)"
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

        elif self._verificar_caracteres_proibidos():
            self.msg_erro = erro_caracter
            self.email_valido = False

        elif "@" in self.email and "." in self.email:
            self._encontrar_posicao_dos_caracteres()

            referencia_um = self.caracteres[0]
            referencia_dois = self.caracteres[1]

            operadora = self.email[referencia_um + 1: referencia_dois]
            final = self.email[referencia_dois + 1:]

            if operadora in self.operadoras_aceitas:
                if final in self.finais_aceitos:

                    try:
                        str(self.email)
                    except Exception as ex:
                        self.msg_erro = f"({ex}):{erro_formato}"
                        self.email_valido = False
                    else:
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

    def _encontrar_posicao_dos_caracteres(self):

        caracteres = ("@", ".")
        lista = list()

        for i in caracteres:
            indice = 0
            while indice < len(self.email):
                if self.email[indice] == i:
                    lista.append(indice)
                indice += 1

        self.caracteres = (lista[0], lista[1])

    def _verificar_caracteres_proibidos(self):
        especiais = ("?", "!", "*", '"', "'", "$", "#", "%")
        acentos = (",", ";", ":", "^", "~")
        textos = ("(", ")", "[", "]", "{", "}", "/", "<", ">")

        proibidos = set(especiais) | set(acentos) | set(textos)

        encontrado = False

        cont = 0
        while cont < len(self.email):
            for i in proibidos:
                if i in self.email:
                    encontrado = True
                    break
                else:
                    continue
            cont += 1

        return encontrado
