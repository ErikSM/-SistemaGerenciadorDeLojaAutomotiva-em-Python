from entrada_de_dados.salvar_modificacoes_no_arquivo import abrir_modificar_e_salvar_arquivo
from estrutura.Cliente import Cliente


def salvar_cliente_em_lista_do_main(cliente: Cliente):
    endereco_do_arquivo = "entrada_de_dados/lista_de_clientes_registrados"

    escrever = _escrever_objeto_cliente(cliente)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_objeto_cliente(cliente: Cliente,):
    nome_da_variavel_do_cliente = _tirar_espacos_do_nome(cliente)
    cpf_da_variavel_do_cliente = _tirar_espacao_do_cpf(cliente)
    return f"\n" \
           f'{cliente.mostrar_dados_do_cliente()}' \
           f'cliente_{nome_da_variavel_do_cliente}' \
           f'{cpf_da_variavel_do_cliente} = Cliente(nome, cpf, telefone, email)' \
           f'\n' \
           f'add_cliente_na_lista_do_main(cliente_{nome_da_variavel_do_cliente}' \
           f'{cpf_da_variavel_do_cliente},' \
           f'"cliente_{nome_da_variavel_do_cliente}{cpf_da_variavel_do_cliente}")' \
           f'\n'


def _tirar_espacos_do_nome(cliente: Cliente):
    nome_espalhado = cliente.nome.split()
    nome_sem_espaco = "_".join(nome_espalhado)
    nome_da_variavel_do_cliente = nome_sem_espaco.lower()
    return nome_da_variavel_do_cliente


def _tirar_espacao_do_cpf(cliente: Cliente):
    cpf_espalhado = cliente.cpf.split()
    cpf_sem_espaco = "_".join(cpf_espalhado)
    cpf_da_variavel_do_cliente = cpf_sem_espaco.lower()
    return cpf_da_variavel_do_cliente
