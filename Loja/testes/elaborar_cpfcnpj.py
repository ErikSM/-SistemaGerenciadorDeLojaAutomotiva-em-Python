from validate_docbr import CPF
from validate_docbr import CNPJ


# exemplo de cpf valido: 52998224725
# exemplo de cnpj valido: 43217051000182
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