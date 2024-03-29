from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral
from estrutura.Loja import Loja


def adicionar_nova_senha_criada_no_arquivo_da_loja(loja: Loja):

    endereco_do_arquivo = "entrada_de_dados/lista_lojas"
    formato = "py"

    escrever = _escrever_senha(loja)
    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_senha(loja: Loja):

    return f'\n' \
           f'{loja.nome_da_variavel}.senha = "{loja.senha}"' \
           f'\n'


def apagar_senha_criada_no_arquivo_da_loja(loja: Loja):

    endereco_do_arquivo = "entrada_de_dados/lista_lojas"
    formato = "py"

    escrever = _apagar_senha(loja)
    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _apagar_senha(loja: Loja):

    return f'\n' \
           f'{loja.nome_da_variavel}.senha = None' \
           f'\n'
