import tkinter



#   ????????   em Construcao  ????????
from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivo, contar_linhas_de_um_arquivo


def _escrever_cargo_em_arquivo(cargo, salario, bonus, comissao, cnpj, linha):
    return f'\n' \
           f'# {cargo}    \n' \
           f'nome = "{cargo}"    \n' \
           f'sarario = "{salario}"    \n' \
           f'bonus = {float(bonus)}    \n' \
           f'comissao = {float(comissao)}    \n' \
           f'cnpj = "{str(cnpj)}"    \n' \
           f'linha = {int(linha)}\n' \
           f'criar_profissao(nome, salario, bonus, comissao, cnpj, linha)    \n' \
           f''


def adicionar_cargo_em_cargos_e_salarios(cargo, salario, bonus, comissao, cnpj):
    endereco_do_arquivo = "cargos_e_salarios"

    formato = "py"

    linha = contar_linhas_de_um_arquivo(endereco_do_arquivo, formato) + 2

    escrever = _escrever_cargo_em_arquivo(cargo, salario, bonus, comissao, cnpj, linha)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, formato, escrever)


adicionar_cargo_em_cargos_e_salarios("advogado", 6000, 0, 0, 124134100000)
