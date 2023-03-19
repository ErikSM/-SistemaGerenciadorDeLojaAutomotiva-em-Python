def validar(numero):
    if len(numero) == 11:
        return True
    else:
        return False


# exemplo de cpf valido: 52998224725
# exemplo de cnpj valido: 43217051000182
class Cpf:
    def __init__(self, numero):
        numero = str(numero)
        if validar(numero):
            self.cpf = numero
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format_cpf()

    def format_cpf(self):
        parte_um = self.cpf[:3]
        parte_dois = self.cpf[3:6]
        parte_tres = self.cpf[6:9]
        parte_quatro = self.cpf[9:]

        return "{}.{}.{}-{}".format(
            parte_um, parte_dois, parte_tres, parte_quatro)
