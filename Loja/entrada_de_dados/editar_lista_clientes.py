from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral, \
    contar_linhas_de_um_arquivo
from estrutura import Loja
from estrutura.Cliente import Cliente


def salvar_cliente_em_lista(cliente: Cliente, loja: Loja):

    endereco_do_arquivo = "entrada_de_dados/lista_clientes"
    formato = "py"

    linha_no_arquivo = contar_linhas_de_um_arquivo(endereco_do_arquivo, formato) + 2

    escrever = _escrever_objeto_cliente(cliente, loja, linha_no_arquivo)
    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_objeto_cliente(cliente: Cliente, loja: Loja, linha_no_arquivo):

    variavel = f'cliente_{cliente.codigo}'
    classe = 'Cliente(nome, cpf, telefone, email, codigo)'

    return f'' \
           f'{cliente.mostrar_atributos_principais()}' \
           f'{variavel} = {classe}\n' \
           f'add_cliente_em_lista({variavel}, {int(loja.cnpj)}, {linha_no_arquivo})' \
           f'\n'
