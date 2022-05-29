import tkinter

from entrada_de_dados.salvar_dados_adicionados_no_programa import atualizar_informacoes


def salvar_loja_em_lista_do_main(nome, cnpj, telefone):
    texto_temporario = tkinter.Text()

    arquivo = open("entrada_de_dados/lista_de_lojas_criadas.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_objeto_loja(nome, cnpj, telefone)

    file = open("entrada_de_dados/lista_de_lojas_criadas.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    texto_temporario.delete(1.0, "end")

    atualizar_informacoes(arquivo, file)

    arquivo.close()
    file.close()


def _escrever_objeto_loja(nome, cnpj, telefone):
    nome_espalhado = nome.split()
    nome_sem_espaco = "_".join(nome_espalhado)
    nome_da_variavel_da_loja = nome_sem_espaco.lower()
    return f'\n' \
           f'nome = "{nome}"\n' \
           f'cnpj = "{cnpj}"\n' \
           f'telefone = "{telefone}"\n' \
           f'loja_{nome_da_variavel_da_loja} = Loja(nome, cnpj, telefone)\n' \
           f'add_loja_na_lista_do_main(loja_{nome_da_variavel_da_loja}, variavel_contador_de_posicao_na_lista)\n' \
           f'variavel_contador_de_posicao_na_lista += 1' \
           f'\n'

