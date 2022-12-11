from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivo, tirar_espacos_e_maiusculas
from estrutura import Loja
from estrutura.Funcionario import Funcionario


def salvar_funcionario_em_lista(funcionario: Funcionario, loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_funcionarios"

    formato = "py"

    escrever = _escrever_objeto_funcionario(funcionario, loja)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, formato, escrever)


def _escrever_objeto_funcionario(funcionario: Funcionario, loja: Loja):
    nome_do_funcionario = tirar_espacos_e_maiusculas(funcionario.nome)
    cpf_do_funcionario = tirar_espacos_e_maiusculas(funcionario.cpf)

    variavel_da_classe = f'funcionario_{nome_do_funcionario}{cpf_do_funcionario}'
    classe = 'Funcionario(nome, cpf, telefone, email, cargo)'

    return f'' \
           f'{funcionario.mostrar_atributos_principais()}' \
           f'{variavel_da_classe} = {classe}\n' \
           f'add_funcionario_na_lista({variavel_da_classe}, \n' \
           f'                         "{variavel_da_classe }", {int(loja.cnpj)})' \
           f'\n'
