from entrada_de_dados.lista_de_vendas_efetuadas import vendas_registradas


def criar_relatorio_de_lucro_total_de_vendas():
    total_venda = _calcular_total_bruto_de_vendas()
    total_gasto = _calcular_gastos_totais_com_obtencao_de_veiculos()
    total_comissao = _calcular_valores_pagos_em_comissao_sobre_a_venda()
    resultado = _calcular_lucro_total_de_vendas()

    return _escrever_relatorio_de_lucro(total_venda, total_gasto, total_comissao, resultado)


def _calcular_total_bruto_de_vendas():
    total_venda = 0
    for i in vendas_registradas:
        variavel = i.preco.split()
        venda_sem_espaco = "".join(variavel)
        venda = float(venda_sem_espaco)
        total_venda += venda

    return total_venda


def _calcular_gastos_totais_com_obtencao_de_veiculos():
    total_gasto = 0
    for i in vendas_registradas:
        variavel = i.veiculo.valor_de_aquisicao.split()
        gasto_sem_espaco = "".join(variavel)
        gasto = float(gasto_sem_espaco)
        total_gasto += gasto

    return total_gasto


def _calcular_valores_pagos_em_comissao_sobre_a_venda():
    total_comissao = 0
    for i in vendas_registradas:
        comissao = i.comissao_sobre_a_venda
        total_comissao += comissao

    return total_comissao


def _calcular_lucro_total_de_vendas():
    total_lucro = 0
    for i in vendas_registradas:
        lucro = float(i.lucro_sobre_a_venda)
        total_lucro += lucro
    return total_lucro


def _escrever_relatorio_de_lucro(total_venda, total_gasto, total_comissao, resultado):
    return f'\n' \
           f'{" " * 10}(( Relatorio de Lucro ))         \n' \
           f'\n' \
           f'\n' \
           f'>> Valor bruto ganho em vendas:             +  R${total_venda:.2f}\n' \
           f'>> Despesas com obtencao de veiculos:       -  R${total_gasto:.2f}\n' \
           f'>> Valor pago em comissao de vendas:        -  R${total_comissao:.2f}\n'\
           f'\n                                              __________\n' \
           f'     ** Lucro Total com Vendas:                R${resultado:.2f}\n' \
           f'\n' \
           f'{"-" * 98}' \
           f'\n'
