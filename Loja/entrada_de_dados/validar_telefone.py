
class Telefone:

    def __init__(self, numero):

        self.telefone = numero

        self.telefone_valido = bool()
        self.mensagem_de_erro = str()

    def __str__(self):
        if len(self.telefone) == 13:
            return self.mascarar_telefone_movel()
        else:
            return self.mascarar_telefone_fixo()

    def validar(self):
        numero = str(self.telefone)

        try:
            int(numero)
        except Exception as ex:
            self.mensagem_de_erro = ex
            self.telefone_valido = False
            return self.telefone_valido

        if len(numero) == 13 or len(numero) == 12:
            self.telefone_valido = True
            return self.telefone_valido
        else:
            self.telefone_valido = False
            return self.telefone_valido

    def mascarar_telefone_fixo(self):
        parte_um = "55"
        parte_dois = self.telefone[0:2]
        parte_tres = self.telefone[2:6]
        parte_quatro = self.telefone[6:]

        return "+{}({}){}-{}".format(
            parte_um, parte_dois, parte_tres, parte_quatro)

    def mascarar_telefone_movel(self):
        parte_um = "55"
        parte_dois = self.telefone[0:2]
        parte_tres = self.telefone[2:7]
        parte_quatro = self.telefone[7:]

        return "+{}({}){}-{}".format(
            parte_um, parte_dois, parte_tres, parte_quatro)
