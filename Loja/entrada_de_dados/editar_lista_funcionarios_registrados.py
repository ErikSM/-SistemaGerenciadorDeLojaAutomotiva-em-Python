from entrada_de_dados.salvar_modificacoes_no_arquivo import abrir_modificar_e_salvar_arquivo
from estrutura.Funcionario import Funcionario


def salvar_funcionario_em_lista_do_main(funcionario: Funcionario):
    endereco_do_arquivo = "entrada_de_dados/lista_de_funcionarios_registrados"

    escrever = _escrever_objeto_funcionario(funcionario)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_objeto_funcionario(funcionario: Funcionario):
    nome_da_variavel_do_funcionario = _tirar_espacos_do_nome(funcionario)
    cpf_da_variavel_do_funcionario = _tirar_espacao_do_cpf(funcionario)
    return f"\n" \
           f'{funcionario.mostrar_atributos_principais()}' \
           f'funcionario_{nome_da_variavel_do_funcionario}' \
           f'{cpf_da_variavel_do_funcionario} = Funcionario(nome, cpf, telefone, email, cargo)' \
           f'\n' \
           f'add_funcionario_na_lista_do_main(funcionario_{nome_da_variavel_do_funcionario}' \
           f'{cpf_da_variavel_do_funcionario}, ' \
           f'"funcionario_{nome_da_variavel_do_funcionario}{cpf_da_variavel_do_funcionario}")' \
           f'\n'


def _tirar_espacos_do_nome(funcionario):
    nome_espalhado = funcionario.nome.split()
    nome_sem_espaco = "_".join(nome_espalhado)
    nome_da_variavel_do_funcionario = nome_sem_espaco.lower()
    return nome_da_variavel_do_funcionario


def _tirar_espacao_do_cpf(funcionario: Funcionario):
    cpf_espalhado = funcionario.cpf.split()
    cpf_sem_espaco = "_".join(cpf_espalhado)
    cpf_da_variavel_do_funcionario = cpf_sem_espaco.lower()
    return cpf_da_variavel_do_funcionario
