from entrada_de_dados.salvar_modificacoes_no_arquivo import abrir_modificar_e_salvar_arquivo
from estrutura.Loja import Loja


def salvar_loja_em_lista_do_main(nome, cnpj, telefone):
    endereco_do_arquivo = "entrada_de_dados/lista_de_lojas_criadas"

    escrever = _escrever_objeto_loja(nome, cnpj, telefone)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_objeto_loja(nome, cnpj, telefone):
    nome_da_variavel_da_loja = _nome_sem_espaco(nome)
    return f'\n' \
           f'nome = "{nome}"\n' \
           f'cnpj = "{cnpj}"\n' \
           f'telefone = "{telefone}"\n' \
           f'loja_{nome_da_variavel_da_loja} = Loja(nome, cnpj, telefone)\n' \
           f'add_loja_na_lista_do_main(loja_{nome_da_variavel_da_loja}, ' \
           f'"loja_{nome_da_variavel_da_loja}")\n' \
           f'_atualizar_contador_da_lista()' \
           f'\n'


def _nome_sem_espaco(nome):
    nome_espalhado = nome.split()
    nome_sem_espaco = "_".join(nome_espalhado)
    nome_da_variavel_da_loja = nome_sem_espaco.lower()
    return nome_da_variavel_da_loja


def remover_loja_da_lista_de_lojas_registrados(loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_de_lojas_criadas"

    escrever = _escrever_remocao_de_loja(loja)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_remocao_de_loja(loja: Loja):
    return f'\n' \
           f'remover_loja_da_lista({loja})' \
           f'\n'
