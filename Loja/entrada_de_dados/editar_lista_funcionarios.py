from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral, tirar_espacos_e_maiusculas, \
    contar_linhas_de_um_arquivo
from estrutura import Loja
from estrutura.Funcionario import Funcionario


def salvar_funcionario_em_lista(funcionario: Funcionario, loja: Loja):

    endereco_do_arquivo = "entrada_de_dados/lista_funcionarios"
    formato = "py"

    linha_no_arquivo = contar_linhas_de_um_arquivo(endereco_do_arquivo, formato) + 2

    escrever = _escrever_objeto_funcionario(funcionario, loja, linha_no_arquivo)
    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_objeto_funcionario(funcionario: Funcionario, loja: Loja, linha_no_arquivo):

    variavel_da_classe = f'funcionario_{funcionario.codigo}'
    classe = 'Funcionario(nome, cpf, telefone, email, codigo)'

    return f'' \
           f'{funcionario.mostrar_atributos_principais()}' \
           f'{variavel_da_classe} = {classe}\n' \
           f'{variavel_da_classe}.cargo = "{funcionario.cargo}"\n' \
           f'add_funcionario_na_lista({variavel_da_classe}, ' \
           f'{int(loja.cnpj)}, {linha_no_arquivo})' \
           f'\n'

