from testes.teste_elaboracao import _teste_gerador_de_codigo, teste_criar_codigo_unico


def test_gerar():
    assert _teste_gerador_de_codigo()


def test_criar():
    assert teste_criar_codigo_unico()
