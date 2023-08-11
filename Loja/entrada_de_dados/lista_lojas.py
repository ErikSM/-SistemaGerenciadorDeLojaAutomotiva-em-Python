from entrada_de_dados.lista_carros import carros_registrados
from entrada_de_dados.lista_clientes import clientes_registrados
from entrada_de_dados.lista_funcionarios import funcionarios_registrados
from entrada_de_dados.lista_vendas import vendas_registradas
from estrutura.Loja import Loja

lojas_registradas = list()


def add_loja_na_lista(loja: Loja, variavel):
    loja.nome_da_variavel = variavel
    lojas_registradas.append(loja)
    _atualizar_contador_da_lista()
    _preencher_listas_de_registros_da_loja(loja)


def _preencher_listas_de_registros_da_loja(loja: Loja):

    for i in carros_registrados:
        if i.cnpj_loja == int(loja.cnpj):
            loja.adicionar_carro(i)

    for i in clientes_registrados:
        if i.cnpj_loja == int(loja.cnpj):
            loja.adicionar_cliente(i)

    for i in funcionarios_registrados:
        if i.cnpj_loja == int(loja.cnpj):
            loja.adicionar_funcionario(i)

    for i in vendas_registradas:
        if int(i.loja.cnpj) == int(loja.cnpj):
            loja.adicionar_venda(i)


def _atualizar_contador_da_lista():

    variavel_contador_de_posicao_na_lista = 0

    for i in lojas_registradas:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


def remover_loja_da_lista(loja):
    lojas_registradas.remove(loja)
    _atualizar_contador_da_lista()


# ------------------ ---------------------- -------------------- -------


nome = "Test Store"
cnpj = "124134100000"
telefone = "99881343425"
loja_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista(loja_test_store, "loja_test_store")

nome = "Secound Test Store"
cnpj = "823765760000"
telefone = "99885434217"
loja_secound_test_store = Loja(nome, cnpj, telefone)
add_loja_na_lista(loja_secound_test_store, "loja_secound_test_store")
