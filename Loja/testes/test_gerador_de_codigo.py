# CMD:  cd PycharmProjects\Loja\testes
from testes.teste_elaboracao import _test_gerador_de_codigo, test_criar_codigo_unico


def test_gerar():
    assert _test_gerador_de_codigo()


def test_criar():
    assert test_criar_codigo_unico()
