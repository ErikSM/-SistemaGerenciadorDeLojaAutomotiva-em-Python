import tkinter

from entrada_de_dados.salvar_dados_adicionados_no_programa import atualizar_informacoes
from estrutura.Cliente import Cliente


def salvar_cliente_em_lista_do_main(cliente:Cliente):
    texto_temporario = tkinter.Text()

    arquivo = open("entrada_de_dados/lista_de_clientes_registrados.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_objeto_cliente(cliente)

    file = open("entrada_de_dados/lista_de_clientes_registrados.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


def _escrever_objeto_cliente(cliente: Cliente):
    nome_espalhado = cliente.nome.split()
    nome_sem_espaco = "_".join(nome_espalhado)
    nome_da_variavel_do_cliente = nome_sem_espaco.lower()

    cpf_espalhado = cliente.cpf.split()
    cpf_sem_espaco = "_".join(cpf_espalhado)
    cpf_da_variavel_do_cliente = cpf_sem_espaco.lower()
    return f"\n" \
           f'nome = "{cliente.nome}"\n' \
           f'cpf = "{cliente.cpf}"\n' \
           f'telefone = "{cliente.telefone}"\n' \
           f'email = "{cliente.email}"' \
           f'\n' \
           f'cliente_{nome_da_variavel_do_cliente}' \
           f'{cpf_da_variavel_do_cliente} = Cliente(nome, cpf, telefone, email)' \
           f'\n' \
           f'add_cliente_na_lista_do_main(cliente_{nome_da_variavel_do_cliente}' \
           f'{cpf_da_variavel_do_cliente}, variavel_contador_de_posicao_na_lista)' \
           f'\n' \
           f'variavel_contador_de_posicao_na_lista += 1' \
           f'\n'
