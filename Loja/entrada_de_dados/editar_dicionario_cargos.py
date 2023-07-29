
from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral, contar_linhas_de_um_arquivo
from estrutura.Cargo import Cargo
from estrutura.Loja import Loja


def adicionar_cargo_em_dicionario_cargos(cargo: Cargo):
    endereco_do_arquivo = "entrada_de_dados/dicionario_cargos"

    formato = "py"

    linha_no_arquivo = contar_linhas_de_um_arquivo(endereco_do_arquivo, formato) + 2

    escrever = _escrever_cargo_em_arquivo(cargo, linha_no_arquivo)

    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_cargo_em_arquivo(cargo: Cargo, linha_no_arquivo):
    return f'\n' \
           f'# {cargo.nome}    \n' \
           f'nome = "{str(cargo.nome)}"    \n' \
           f'salario = "{str(cargo.salario)}"    \n' \
           f'bonus = {float(cargo.bonus)}    \n' \
           f'comissao = {float(cargo.comissao)}    \n' \
           f'cnpj = "{str(cargo.cnpj)}"    \n' \
           f'linha = {int(linha_no_arquivo)}    \n' \
           f'criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)    \n' \
           f''


#  kCriando #########
def criar_chave_da_loja_em_dicionario_cargos(loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/dicionario_cargos"

    formato = "py"

    escrever = _escrever_chave_da_loja_em_dicionario(loja)

    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_chave_da_loja_em_dicionario(loja: Loja):
    return f'\n' \
           f'# loja criada    \n' \
           f'dicionario_de_cargos_da_loja["{loja.cnpj}"] = dict()    \n' \
           f''
