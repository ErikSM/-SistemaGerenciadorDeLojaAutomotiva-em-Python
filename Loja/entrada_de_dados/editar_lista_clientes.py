from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivo, tirar_espacos_e_maiusculas
from estrutura.Cliente import Cliente


def salvar_cliente_em_lista(cliente: Cliente):
    endereco_do_arquivo = "entrada_de_dados/lista_clientes"

    escrever = _escrever_objeto_cliente(cliente)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_objeto_cliente(cliente: Cliente,):
    nome_do_cliente = tirar_espacos_e_maiusculas(cliente.nome)
    cpf_do_cliente = tirar_espacos_e_maiusculas(cliente.cpf)

    variavel_da_classe = f'cliente_{nome_do_cliente}{cpf_do_cliente}'
    classe = 'Cliente(nome, cpf, telefone, email)'

    return f'' \
           f'{cliente.mostrar_atributos_principais()}' \
           f'{variavel_da_classe} = {classe}\n' \
           f'add_cliente_na_lista({variavel_da_classe}, "{variavel_da_classe}")' \
           f'\n'
