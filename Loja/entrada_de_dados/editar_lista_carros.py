from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral, \
    contar_linhas_de_um_arquivo

from estrutura import Loja
from estrutura.Carro import Carro


def salvar_carro_em_lista(carro: Carro, loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_carros"

    formato = "py"

    linha_no_arquivo = contar_linhas_de_um_arquivo(endereco_do_arquivo, formato) + 2

    escrever = _escrever_objeto_carro(carro, loja, linha_no_arquivo)

    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_objeto_carro(carro: Carro, loja: Loja, linha_no_arquivo):
    variavel = f'carro_{carro.codigo}'
    classe = 'Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)'

    return f'' \
           f'{carro.mostrar_atributos_principais()}' \
           f'{variavel} = {classe}\n' \
           f'add_carro_na_lista({variavel}, {int(loja.cnpj)}, {linha_no_arquivo})' \
           f'\n'

