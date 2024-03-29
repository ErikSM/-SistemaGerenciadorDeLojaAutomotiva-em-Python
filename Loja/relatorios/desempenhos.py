import tkinter

from ferramentas.Preco import Preco
from relatorios.graficos import construir_grafico_barras
from estrutura import Loja


def comissoes_pagas_por_cada_funcionario(loja: Loja):

    texto_temporario = tkinter.Text()
    texto_temporario.insert(1.0, "\n      ((Comissoes pagas para cada funcionario))\n\n\n")

    dicionario_do_grafico = dict()

    # i == cada_funcionario
    for i in loja.dicionario_da_loja["funcionarios"]:
        texto_temporario.insert("end", f'{i.nome}[{i.cargo["cargo"]}]:')

        # j == cada_comissao
        for j in i.comissoes_recebidas:
            texto_temporario.insert("end", f' + {Preco(j)}')
        texto_temporario.insert("end", f'\ntotal:{Preco(i.total_comissoes_recebidas)}\n\n\n')

        dicionario_do_grafico[f'{i.nome}\n({i.cargo["cargo"]})'] = float(i.total_comissoes_recebidas)

    definicoes_do_grafico = ("Funcionarios:", "Total de comissoes recebidas:", "Desempenho de funcionarios:")
    construir_grafico_barras(dicionario_do_grafico, definicoes_do_grafico, "R$")

    return texto_temporario.get(1.0, "end")
