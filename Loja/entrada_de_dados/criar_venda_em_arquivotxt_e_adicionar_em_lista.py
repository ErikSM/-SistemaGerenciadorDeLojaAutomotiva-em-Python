import tkinter

from entrada_de_dados.salvar_dados_adicionados_no_programa import atualizar_informacoes
from estrutura.Venda import Venda
from estrutura.Carro import Carro


def _escrever_relatorio_de_venda_em_texto(venda: Venda):
    venda = venda
    return f'{venda}' \
           f'\n'


def criar_relatorio_de_venda_em_arquivo_de_texto(venda: Venda, codigo):
    open(f"../relatorios_de_venda/venda_codigo_{codigo}.py", "x")

    venda = venda
    texto_temporario = tkinter.Text()

    arquivo = open(f"../relatorios_de_venda/venda_codigo_{codigo}.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_relatorio_de_venda_em_texto(venda)

    file = open(f"../relatorios_de_venda/venda_codigo_{codigo}.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    file.close()


def _escrever_relatorio_em_lista_do_main(codigo):
    return f'\n' \
           f'from relatorios_de_venda.venda_codigo_{codigo} import venda_{codigo}\n' \
           f'add_venda_na_lista_do_main(venda_{codigo})' \
           f'\n'


def adicionar_relatorio_de_venda_em_lista_do_main(codigo):
    texto_temporario = tkinter.Text()

    arquivo = open("../entrada_de_dados/lista_de_vendas_efetuadas.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_relatorio_em_lista_do_main(codigo)

    file = open("../entrada_de_dados/lista_de_vendas_efetuadas.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


def _escrever_remocao_de_carro_vendido(carro: Carro):

    return f'\n' \
           f'remover_carro_da_lista({carro})' \
           f'\n'


def remover_carro_vendido_da_lista_de_carros_registrados(carro: Carro):
    texto_temporario = tkinter.Text()

    arquivo = open("../entrada_de_dados/lista_de_carros_registrados.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_remocao_de_carro_vendido(carro)

    file = open("../entrada_de_dados/lista_de_carros_registrados.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()
