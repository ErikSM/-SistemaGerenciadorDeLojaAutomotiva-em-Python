from validate_docbr import CPF
from validate_docbr import CNPJ


# exemplo de cpf valido: 52998224725
# exemplo de cnpj valido: 43217051000182
# ----------  --------------------   ------------------
class ElaborarDocumento:

    def __init__(self, numero):

        self.documento = numero

        self.mascarado = str()
        self.documento_valido = bool()

    def __str__(self):
        if len(self.documento) == 11:
            self._mascara_cpf()
            return self.mascarado
        elif len(self.documento) == 14:
            self._mascara_cnpj()
            return self.mascarado
        else:
            return self.documento

    def validade(self):
        try:
            int(self.documento)
        except ValueError:
            self.documento_valido = False
        else:
            if len(self.documento) == 11:
                self._mascara_cpf()
                self.documento_valido = self._validade_cpf()
            elif len(self.documento) == 14:
                self._mascara_cnpj()
                self.documento_valido = self._validade_cnpj()
            else:
                self.documento_valido = False

        return self.documento_valido

    def _mascara_cpf(self):
        mascara = CPF()
        self.mascarado = mascara.mask(self.documento)

    def _validade_cpf(self):
        validar = CPF()
        cpf_valido = validar.validate(self.mascarado)
        return cpf_valido

    def _mascara_cnpj(self):
        mascara = CNPJ()
        self.mascarado = mascara.mask(self.documento)

    def _validade_cnpj(self):
        validar = CNPJ()
        cnpj_valido = validar.validate(self.mascarado)
        return cnpj_valido


# -----------  ------------  ------------  ---------------


def averiguar_documento(numero):
    if len(numero) == 14 or len(numero) == 11:

        if len(numero) == 14:
            mascarado = _mascara_cnpj(numero)
            print(mascarado)
            cnpj = _validade_cnpj(mascarado)
            if cnpj:
                print("cnpj valido")
            else:
                print("cnpj Error")

        if len(numero) == 11:
            mascarado = _mascara_cpf(numero)
            print(mascarado)
            cpf = _validade_cpf(mascarado)
            if cpf:
                print("cpf valido")
            else:
                print("cpf Error")

    else:
        print("Doc invalido")


# cpf
def _mascara_cpf(numero):
    mascara = CPF()
    return mascara.mask(numero)


def _validade_cpf(numero_mascarado):
    validar = CPF()
    return validar.validate(numero_mascarado)


# cnpj
def _mascara_cnpj(numero):
    mascara = CNPJ()
    return mascara.mask(numero)


def _validade_cnpj(numero_mascarado):
    validar = CNPJ()
    return validar.validate(numero_mascarado)


averiguar_documento("60746948000112")
print("-"*20)
print(ElaborarDocumento("60746948000112"))
print(ElaborarDocumento("60746948000112").validade())
