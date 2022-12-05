import tkinter

from estrutura import Loja


def criar_relatorio_de_comissoes_pagas_por_cada_funcionario(loja: Loja):
    texto_temporario = tkinter.Text()
    texto_temporario.insert(1.0, "\n      ((Comissoes pagas para cada funcionario))\n\n\n")

    for funcionario in loja.dicionario_da_loja["funcionarios"]:
        texto_temporario.insert("end", f'{funcionario.nome}[{funcionario.cargo["cargo"]}]:')
        for comissao in funcionario.comissoes_recebidas:
            texto_temporario.insert("end", f' + R${float(comissao):.2f}')
        texto_temporario.insert("end", f'\ntotal:R${float(funcionario.total_comissoes_recebidas):.2f}\n\n\n')

    return texto_temporario.get(1.0, "end")


