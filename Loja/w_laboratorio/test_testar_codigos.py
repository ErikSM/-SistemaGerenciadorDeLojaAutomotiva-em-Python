# CMD:  cd PycharmProjects\Loja\w_laboratorio
from w_laboratorio.elaborar_cpfcnpj import averiguar_documento
from w_laboratorio.elaborar_gerador_codigo import _elaborar_gerador_de_codigo, elaborar_criar_codigo_unico
from w_laboratorio.elaborar_telefone import TelefoneTeste


def test_gerar_codigo():
    assert _elaborar_gerador_de_codigo()


def test_criar_codigo():
    assert elaborar_criar_codigo_unico()


def test_averiguar_documento():
    return averiguar_documento("60746948000112")


treze = "1234543456789"
doze = "234544444444"


def test_mascarar_telefone():
    assert TelefoneTeste(doze)

