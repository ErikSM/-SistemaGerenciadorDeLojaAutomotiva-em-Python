# CMD:  cd PycharmProjects\Loja\testes
from testes.elaborar_cpfcnpj import averiguar_documento
from testes.elaborar_gerador_codigo import _test_gerador_de_codigo, test_criar_codigo_unico
from testes.elaborar_telefone import TelefoneTeste


def test_gerar_codigo():
    assert _test_gerador_de_codigo()


def test_criar_codigo():
    assert test_criar_codigo_unico()


def test_averiguar_documento():
    return averiguar_documento("60746948000112")


treze = "1234543456789"
doze = "234544444444"


def test_mascarar_telefone():
    assert TelefoneTeste(doze)

