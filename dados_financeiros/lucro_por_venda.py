import tkinter

from entrada_de_dados.lista_de_vendas_efetuadas import vendas_registradas


def calcular_lucro_sobre_a_venda_por_cada_veiculo():
    texto_temporario = tkinter.Text()
    texto_temporario.insert(1.0, "\n      ((Lucro por cada venda))\n\n\n")
    for i in vendas_registradas:
        codigo = i.codigo
        data = i.data
        valor_gasto = i.veiculo.valor_de_aquisicao
        valor_ganho = i.preco
        lucro = int("".join(valor_ganho.split())) - int("".join(valor_gasto.split()))
        texto_temporario.insert("end", _escrever_lucro_sobre_a_venda(codigo, data, valor_gasto, valor_ganho, lucro))
    return texto_temporario.get(1.0, "end")


def _escrever_lucro_sobre_a_venda(codigo, data, valor_gasto, valor_ganho, lucro):
    return f'\n' \
           f'   >> Codigo de Venda:{codigo} <<\n' \
           f'\n' \
           f'data:{data}   ' \
           f'valor de aquisicao: R${valor_gasto}   ' \
           f'valor de venda: R${valor_ganho}   ' \
           f'**Lucro: R${lucro}**\n' \
           f'\n' \
           f'{"-"*196}' \
           f'\n'
