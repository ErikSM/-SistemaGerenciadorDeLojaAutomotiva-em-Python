from entrada_de_dados.lista_de_vendas_efetuadas import vendas_registradas


def calcular_lucro_total_de_vendas():

    total_venda = _calcular_total_bruto_de_vendas()
    total_gasto = _calcular_gastos_totais_com_obtencao_de_veiculos()

    resultado = (int(total_venda) - int(total_gasto))

    return _escrever_relatorio_de_lucro(total_venda, total_gasto, resultado)


def _calcular_total_bruto_de_vendas():
    total_venda = 0
    for i in vendas_registradas:
        variavel = i.preco.split()
        venda_sem_espaco = "".join(variavel)
        venda = int(venda_sem_espaco)
        total_venda += venda

    return total_venda


def _calcular_gastos_totais_com_obtencao_de_veiculos():
    total_gasto = 0
    for i in vendas_registradas:
        variavel = i.veiculo.valor_de_aquisicao.split()
        gasto_sem_espaco = "".join(variavel)
        gasto = int(gasto_sem_espaco)
        total_gasto += gasto

    return total_gasto


def _escrever_relatorio_de_lucro(total_venda, total_gasto, resultado):
    return f'\n' \
           f'{" "*10}(( Relatorio de Lucro ))         \n' \
           f'\n' \
           f'\n' \
           f'>> Valor bruto ganho em vendas:               R${total_venda}\n' \
           f'>> Despesas com obtencao de veiculos:         R${total_gasto}\n' \
           f'\n                                              __________\n' \
           f'     ** Lucro Total com Vendas:                R${resultado}\n' \
           f'\n' \
           f'{"-"*98}' \
           f'\n'
