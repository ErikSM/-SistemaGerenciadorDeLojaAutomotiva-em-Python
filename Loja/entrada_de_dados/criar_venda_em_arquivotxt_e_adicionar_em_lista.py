import tkinter


from estrutura.Venda import Venda


def _escrever_relatorio_em_lista_do_main(codigo):
    return f'\n' \
           f'from relatorios_de_venda.venda_codigo_{codigo} import venda_{codigo}\n' \
           f'add_venda_na_lista_do_main(venda_{codigo})\n' \
           f'\n'


def _escrever_relatorio_de_venda_em_texto(venda: Venda):
    venda = venda
    return f'{venda}' \
           f'\n'


def criar_relatorio_de_venda_em_arquivo_de_texto(venda: Venda, codigo):
    open(f"../relatorios_de_venda/venda_codigo_{codigo}.py", "x")

    venda = venda
    texto_temporario = tkinter.Text()

    file = open(f"../relatorios_de_venda/venda_codigo_{codigo}.py", "r")
    arquivo_lido = file.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_relatorio_de_venda_em_texto(venda)

    file = open(f"../relatorios_de_venda/venda_codigo_{codigo}.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    texto_temporario.delete(1.0, "end")
    file.close()


def adicionar_relatorio_de_venda_em_lista_do_main(codigo):

    texto_temporario = tkinter.Text()

    file = open("../entrada_de_dados/lista_de_vendas_efetuadas.py", "r")
    arquivo_lido = file.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_relatorio_em_lista_do_main(codigo)

    file = open("../entrada_de_dados/lista_de_vendas_efetuadas.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    texto_temporario.delete(1.0, "end")
    file.close()



