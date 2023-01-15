
from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivo, contar_linhas_de_um_arquivo
from estrutura.Cargo import Cargo


def adicionar_cargo_em_cargos_e_salarios(cargo: Cargo):
    endereco_do_arquivo = "entrada_de_dados/cargos_e_salarios"

    formato = "py"

    linha_no_arquivo = contar_linhas_de_um_arquivo(endereco_do_arquivo, formato) + 2

    escrever = _escrever_cargo_em_arquivo(cargo, linha_no_arquivo)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, formato, escrever)


def _escrever_cargo_em_arquivo(cargo: Cargo, linha_no_arquivo):
    return f'\n' \
           f'# {cargo.nome}    \n' \
           f'nome = "{cargo.nome}"    \n' \
           f'salario = "{cargo.salario}"    \n' \
           f'bonus = {float(cargo.bonus)}    \n' \
           f'comissao = {float(cargo.comissao)}    \n' \
           f'cnpj = "{str(cargo.cnpj)}"    \n' \
           f'linha = {int(linha_no_arquivo)}    \n' \
           f'criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)    \n' \
           f''

