from validate_docbr import CPF
from validate_docbr import CNPJ


def verificar_documento(numero):
    if len(numero) == 14 or len(numero) == 11:

        if len(numero) == 14:
            mascarado = mascarar_cnpj(numero)
            cnpj = _validar_cnpj(mascarado)
            if cnpj:
                documento_valido = cnpj

            else:
                documento_valido = False

        if len(numero) == 11:
            mascarado = mascarar_cpf(numero)
            cpf = _validar_cpf(mascarado)
            if cpf:
                documento_valido = cpf
            else:
                documento_valido = False

    else:
        documento_valido = False

    return documento_valido


# cpf
def mascarar_cpf(numero):
    mascara = CPF()
    return mascara.mask(numero)


def _validar_cpf(numero_mascarado):
    validar = CPF()
    return validar.validate(numero_mascarado)


# cnpj
def mascarar_cnpj(numero):
    mascara = CNPJ()
    return mascara.mask(numero)


def _validar_cnpj(numero_mascarado):
    validar = CNPJ()
    return validar.validate(numero_mascarado)

