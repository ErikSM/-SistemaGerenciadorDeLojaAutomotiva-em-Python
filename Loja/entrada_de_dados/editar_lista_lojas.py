from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral, tirar_espacos_e_maiusculas
from estrutura.Loja import Loja


def salvar_loja_em_lista(loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_lojas"
    formato = "py"

    escrever = _escrever_objeto_loja(loja)
    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_objeto_loja(loja: Loja):

    variavel_da_classe = f'loja_{loja.codigo}'
    classe = 'Loja(nome, cnpj, telefone, email, codigo)'

    return f'\n' \
           f'nome = "{loja.nome}"\n' \
           f'cnpj = "{loja.cnpj}"\n' \
           f'telefone = "{loja.telefone}"\n' \
           f'email = "{loja.email}"\n' \
           f'codigo = "{loja.codigo}"' \
           f'\n' \
           f'{variavel_da_classe} = {classe}' \
           f'\n' \
           f'add_loja_na_lista({variavel_da_classe})\n' \
           f''


def remover_loja_da_lista(loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_lojas"
    formato = "py"

    escrever = _escrever_remocao_de_loja(loja)
    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_remocao_de_loja(loja: Loja):
    return f'\n' \
           f'remover_loja_da_lista({loja})' \
           f'\n'
