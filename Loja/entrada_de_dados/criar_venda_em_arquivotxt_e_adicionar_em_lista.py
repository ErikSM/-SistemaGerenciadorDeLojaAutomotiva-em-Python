import tkinter

from entrada_de_dados.salvar_dados_adicionados_no_programa import atualizar_informacoes
from estrutura.Venda import Venda
from estrutura.Carro import Carro


def adicionar_relatorio_de_venda_em_lista_do_main(venda: Venda):

    texto_temporario = tkinter.Text()

    arquivo = open("entrada_de_dados/lista_de_vendas_efetuadas.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_venda(venda)

    file = open("entrada_de_dados/lista_de_vendas_efetuadas.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


def _escrever_venda(venda: Venda):
    venda = venda
    return f'\n' \
           f'{venda}' \
           f'\n' \
           f'add_venda_na_lista_do_main(venda_{venda.codigo})\n\n' \
           f'# -------------------------------------------------------\n' \
           f'\n'


def remover_carro_vendido_da_lista_de_carros_registrados(carro: Carro, codigo):
    texto_temporario = tkinter.Text()

    arquivo = open("entrada_de_dados/lista_de_carros_registrados.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_remocao_de_carro_vendido(carro, codigo)

    file = open("entrada_de_dados/lista_de_carros_registrados.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


def _escrever_remocao_de_carro_vendido(carro: Carro, codigo):
    return f'\n' \
           f'remover_carro_da_lista({carro}, "{codigo}")' \
           f'\n'
