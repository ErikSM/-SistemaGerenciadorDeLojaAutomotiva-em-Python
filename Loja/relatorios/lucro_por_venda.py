import tkinter

from relatorios.graficos import construir_grafico_barras
from estrutura import Loja


def criar_relatorio_de_lucro_sobre_a_venda_por_cada_veiculo(loja: Loja):
    texto_temporario = tkinter.Text()
    texto_temporario.insert(1.0, "\n      ((Lucro por cada venda))\n\n\n")

    dicionario_do_grafico = dict()

    for venda in loja.dicionario_da_loja["vendas"]:
        codigo = venda.codigo
        data = venda.data
        valor_gasto = float("".join(venda.veiculo.valor_de_aquisicao.split()))
        valor_ganho = float("".join(venda.preco.split()))
        comissao = venda.comissao_sobre_a_venda
        lucro = venda.lucro_sobre_a_venda
        texto_temporario.insert("end", _escrever_lucro_sobre_a_venda(codigo,
                                                                     data, valor_gasto, valor_ganho, comissao, lucro))

        # construindo grafico
        dicionario_do_grafico[venda.codigo] = venda.lucro_sobre_a_venda
    construir_grafico_barras(dicionario_do_grafico, "Codigo da venda", "Lucro com a venda", "Historico de lucro", "R$")

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
           f'{"-" * 196}' \
           f'\n'
