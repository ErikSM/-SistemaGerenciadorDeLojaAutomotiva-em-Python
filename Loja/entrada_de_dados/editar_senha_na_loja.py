from entrada_de_dados.salvar_modificacoes_no_arquivo import abrir_modificar_e_salvar_arquivo
from estrutura.Loja import Loja


def adicionar_nova_senha_criada_no_arquivo_da_loja(loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_de_lojas_criadas"

    escrever = _escrever_senha(loja)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_senha(loja: Loja):
    return f'\n' \
           f'{loja.nome_da_variavel}.senha = "{loja.senha}"' \
           f'\n'


def apagar_senha_criada_no_arquivo_da_loja(loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_de_lojas_criadas"

    escrever = _apagar_senha(loja)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _apagar_senha(loja: Loja):
    return f'\n' \
           f'{loja.nome_da_variavel}.senha = None' \
           f'\n'
