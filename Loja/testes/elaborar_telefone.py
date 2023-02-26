def validar(numero):
    numero = str(numero)
    if len(numero) == 13 or len(numero) == 12:
        return True
    else:
        return False


class TelefoneTeste:
    def __init__(self, numero):

        self.cpf = None

        if validar(numero):
            self.cpf = numero
        else:
            raise ValueError("Numero invalido!")

    def __str__(self):
        if len(self.cpf) == 12:
            return self.format_telefone_fixo()
        else:
            return self.format_telefone_movel()

    def format_telefone_fixo(self):
        parte_um = self.cpf[:2]
        parte_dois = self.cpf[2:4]
        parte_tres = self.cpf[4:8]
        parte_quatro = self.cpf[8:]

        return "+{}({}){}-{}".format(
            parte_um, parte_dois, parte_tres, parte_quatro)

    def format_telefone_movel(self):
        parte_um = self.cpf[:2]
        parte_dois = self.cpf[2:4]
        parte_tres = self.cpf[4:9]
        parte_quatro = self.cpf[9:]

        return "+{}({}){}-{}".format(
            parte_um, parte_dois, parte_tres, parte_quatro)


treze = "1234543456789"
doze = "234544444444"

print(TelefoneTeste(treze))
