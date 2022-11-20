
# teste
'''
def validar(numero):
    numero = str(numero)
    if len(numero) == 13 or len(numero) == 12:
        return True
    else:
        return False
        '''


class Telefone:
    def __init__(self, numero):

        self.cpf = numero

        # Teste
        '''if validar(numero):
            self.cpf = numero
        else:
            raise ValueError("Numero invalido!")'''

    def __str__(self):
        if len(self.cpf) == 13:
            return self.telefone_movel()
        else:
            return self.telefone_fixo()

    def telefone_fixo(self):
        parte_um = "55"
        parte_dois = self.cpf[0:2]
        parte_tres = self.cpf[2:6]
        parte_quatro = self.cpf[6:]

        return "+{}({}){}-{}".format(
            parte_um, parte_dois, parte_tres, parte_quatro)

    def telefone_movel(self):
        parte_um = "55"
        parte_dois = self.cpf[0:2]
        parte_tres = self.cpf[2:7]
        parte_quatro = self.cpf[7:]

        return "+{}({}){}-{}".format(
            parte_um, parte_dois, parte_tres, parte_quatro)

