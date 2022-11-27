import tkinter

from entrada_de_dados.lista_vendas import vendas_registradas


def criar_relatorio_de_lucro_sobre_a_venda_por_cada_veiculo():
    texto_temporario = tkinter.Text()
    texto_temporario.insert(1.0, "\n      ((Lucro por cada venda))\n\n\n")
    for i in vendas_registradas:
        codigo = i.codigo
        data = i.data
        valor_gasto = float("".join(i.veiculo.valor_de_aquisicao.split()))
        valor_ganho = float("".join(i.preco.split()))
        comissao = i.comissao_sobre_a_venda
        lucro = i.lucro_sobre_a_venda
        texto_temporario.insert("end", _escrever_lucro_sobre_a_venda(codigo, data, valor_gasto, valor_ganho, comissao, lucro))
    return texto_temporario.get(1.0, "end")


def _escrever_lucro_sobre_a_venda(codigo, data, valor_gasto, valor_ganho, comissao, lucro):
    return f'\n' \
           f'   >> Codigo de Venda:{codigo} <<\n' \
           f'\n' \
           f'data:{data}\n   ' \
           f'valor de aquisicao: R${valor_gasto:.2f}   ' \
           f'valor de venda: R${valor_ganho:.2f}   ' \
           f'comissao: R${comissao:.2f}   ' \
           f'\n**Lucro: R${lucro:.2f}**\n' \
           f'\n' \
           f'{"-"*196}' \
           f'\n'
