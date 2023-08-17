import tkinter

from ferramentas.Preco import Preco
from relatorios.graficos import construir_grafico_linhas
from estrutura import Loja


def lucro_sobre_a_venda_por_cada_veiculo(loja: Loja):

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

        tupla_de_valores = (valor_gasto, valor_ganho, comissao, lucro)
        texto_temporario.insert("end", _escrever_lucro_sobre_a_venda(codigo, data, tupla_de_valores))

        dicionario_do_grafico[venda.codigo] = venda.lucro_sobre_a_venda

    definicoes_do_grafico = ("Codigo da venda", "Lucro com a venda", "Historico de lucro")
    construir_grafico_linhas(dicionario_do_grafico, definicoes_do_grafico, "R$")

    return texto_temporario.get(1.0, "end")


def _escrever_lucro_sobre_a_venda(codigo, data, tupla_de_valores: tuple):

    valor_gasto = tupla_de_valores[0]
    valor_ganho = tupla_de_valores[1]
    comissao = tupla_de_valores[2]

    lucro = tupla_de_valores[3]

    return f'\n' \
           f'   >> Codigo de Venda:{codigo} <<\n' \
           f'\n' \
           f'data:{data}\n   ' \
           f'valor de aquisicao: {Preco(valor_gasto)}   ' \
           f'valor de venda: {Preco(valor_ganho)}   ' \
           f'comissao: {Preco(comissao)}   ' \
           f'\n**Lucro: {Preco(lucro)}**\n' \
           f'\n' \
           f'{"-" * 196}' \
           f'\n'
