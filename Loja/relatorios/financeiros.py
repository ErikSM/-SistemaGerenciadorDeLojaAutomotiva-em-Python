from ferramentas.Preco import Preco
from relatorios.graficos import construir_grafico_barras
from estrutura import Loja


def lucro_total_de_vendas(loja: Loja):

    dicionario_do_grafico = dict()

    total_venda = _calcular_total_bruto_de_vendas(loja)
    dicionario_do_grafico["Total Recebido"] = total_venda

    total_gasto = _calcular_gastos_totais_com_obtencao_de_veiculos(loja)
    dicionario_do_grafico["Total de Gastos"] = total_gasto

    total_comissao = _calcular_valores_pagos_em_comissao_sobre_a_venda(loja)
    dicionario_do_grafico["Pago em comissoes"] = total_comissao

    resultado_lucro = _calcular_lucro_total_de_vendas(loja)
    dicionario_do_grafico["Lucro com vendas"] = resultado_lucro

    definicoes_do_grafico = ("",
                             "Valores:",
                             "Numeros Totais de Gastos e Lucros")

    construir_grafico_barras(dicionario_do_grafico, definicoes_do_grafico, "R$")

    tupla_do_relatorio = (total_venda,
                          total_gasto,
                          total_comissao,
                          resultado_lucro)


    return _escrever_relatorio_de_lucro(tupla_do_relatorio)


def _calcular_total_bruto_de_vendas(loja: Loja):

    total_venda = 0

    for i in loja.dicionario_da_loja["vendas"]:
        variavel = i.preco.split()
        venda_sem_espaco = "".join(variavel)
        venda = float(venda_sem_espaco)

        total_venda += venda

    return total_venda


def _calcular_gastos_totais_com_obtencao_de_veiculos(loja: Loja):

    total_gasto = 0

    for i in loja.dicionario_da_loja["vendas"]:
        variavel = i.veiculo.valor_de_aquisicao.split()
        gasto_sem_espaco = "".join(variavel)
        gasto = float(gasto_sem_espaco)

        total_gasto += gasto

    return total_gasto


def _calcular_valores_pagos_em_comissao_sobre_a_venda(loja: Loja):

    total_comissao = 0

    for i in loja.dicionario_da_loja["vendas"]:
        comissao = i.comissao_sobre_a_venda

        total_comissao += comissao

    return total_comissao


def _calcular_lucro_total_de_vendas(loja: Loja):

    total_lucro = 0

    for i in loja.dicionario_da_loja["vendas"]:
        lucro = float(i.lucro_sobre_a_venda)

        total_lucro += lucro

    return total_lucro


def _escrever_relatorio_de_lucro(tupla_do_relatorio: tuple):

    total_venda = tupla_do_relatorio[0]
    total_gasto = tupla_do_relatorio[1]
    total_comissao = tupla_do_relatorio[2]

    resultado_lucro = tupla_do_relatorio[3]

    return f'\n' \
           f'{" " * 10}(( Relatorio de Lucro ))         \n' \
           f'\n' \
           f'\n' \
           f'>> Valor bruto ganho em vendas:             +  {Preco(total_venda)}\n' \
           f'>> Despesas com obtencao de veiculos:       -  {Preco(total_gasto)}\n' \
           f'>> Valor pago em comissao de vendas:        -  {Preco(total_comissao)}\n'\
           f'\n                                              __________________\n' \
           f'     ** Lucro Total com Vendas:                {Preco(resultado_lucro)}\n' \
           f'\n' \
           f'{"-" * 98}' \
           f'\n'
