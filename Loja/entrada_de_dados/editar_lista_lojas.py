from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral, tirar_espacos_e_maiusculas
from estrutura.Loja import Loja


def salvar_loja_em_lista(nome, cnpj, telefone):
    endereco_do_arquivo = "entrada_de_dados/lista_lojas"

    formato = "py"

    escrever = _escrever_objeto_loja(nome, cnpj, telefone)

    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_objeto_loja(nome, cnpj, telefone):
    nome_da_loja = tirar_espacos_e_maiusculas(nome)

    variavel_da_classe = f'loja_{nome_da_loja}'
    classe = 'Loja(nome, cnpj, telefone)'

    return f'\n' \
           f'nome = "{nome}"\n' \
           f'cnpj = "{cnpj}"\n' \
           f'telefone = "{telefone}"' \
           f'\n' \
           f'{variavel_da_classe} = {classe}' \
           f'\n' \
           f'add_loja_na_lista({variavel_da_classe}, "{variavel_da_classe}")\n' \
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
