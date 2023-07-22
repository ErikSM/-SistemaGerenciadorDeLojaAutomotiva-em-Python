import tkinter

from relatorios.graficos import construir_grafico_barras
from estrutura import Loja


def criar_relatorio_de_comissoes_pagas_por_cada_funcionario(loja: Loja):

    texto_temporario = tkinter.Text()
    texto_temporario.insert(1.0, "\n      ((Comissoes pagas para cada funcionario))\n\n\n")

    dicionario_do_grafico = dict()

    for i in loja.dicionario_da_loja["funcionarios"]:
        texto_temporario.insert("end", f'{i.nome}[{i.cargo["cargo"]}]:')

        for j in i.comissoes_recebidas:
            texto_temporario.insert("end", f' + R${float(j):.2f}')

        texto_temporario.insert("end", f'\ntotal:R${float(i.total_comissoes_recebidas):.2f}\n\n\n')
        dicionario_do_grafico[f'{i.nome}\n({i.cargo["cargo"]})'] = float(i.total_comissoes_recebidas)

    definicoes_do_grafico = ("Funcionarios:", "Total de comissoes recebidas:", "Desempenho de funcionarios:")
    construir_grafico_barras(dicionario_do_grafico, definicoes_do_grafico,"R$")

    return texto_temporario.get(1.0, "end")
