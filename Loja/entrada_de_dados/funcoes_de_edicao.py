import tkinter

from entrada_de_dados.salvar_modificacoes import atualizar_informacoes


def abrir_modificar_e_salvar_arquivo(endereco, formato, escrever):
    texto_temporario = tkinter.Text()

    arquivo = open(f"{endereco}.{formato}", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = escrever

    file = open(f"{endereco}.{formato}", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


def editar_arquivo_em_opcoes_avancadas(objeto, tipo_de_lista, variavel_editada, novo_conteudo):

    texto_temporario = tkinter.Text()

    parametro_um = None
    parametro_dois = None

    if tipo_de_lista == "carros":
        if variavel_editada == "montadora":
            parametro_um = f"{objeto.linha_no_arquivo}.0"
            parametro_dois = f"{objeto.linha_no_arquivo}.99"
        if variavel_editada == "nome":
            parametro_um = f"{objeto.linha_no_arquivo + 1}.0"
            parametro_dois = f"{objeto.linha_no_arquivo + 1}.99"
    else:
        if variavel_editada == "nome":
            parametro_um = f"{objeto.linha_no_arquivo}.0"
            parametro_dois = f"{objeto.linha_no_arquivo}.99"
        if variavel_editada == "cpf":
            parametro_um = f"{objeto.linha_no_arquivo + 1}.0"
            parametro_dois = f"{objeto.linha_no_arquivo + 1}.99"

    if variavel_editada == "ano" or variavel_editada == "telefone":
        parametro_um = f"{objeto.linha_no_arquivo + 2}.0"
        parametro_dois = f"{objeto.linha_no_arquivo + 2}.99"

    if variavel_editada == "valor_de_aquisicao" or variavel_editada == "email":
        parametro_um = f"{objeto.linha_no_arquivo + 3}.0"
        parametro_dois = f"{objeto.linha_no_arquivo + 3}.99"

    arquivo = open(f"entrada_de_dados/lista_{tipo_de_lista}.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    escrever_variavel_1 = f'{variavel_editada} = "{novo_conteudo}"'

    file = open(f"entrada_de_dados/lista_{tipo_de_lista}.py", "w")
    texto_temporario.delete(float(parametro_um), float(parametro_dois))
    texto_temporario.insert(float(parametro_um), escrever_variavel_1)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


def tirar_espacos_e_maiusculas(string):
    string_espalhada = string.split()
    string_sem_espaco = "_".join(string_espalhada)
    string_em_minuscula = string_sem_espaco.lower()
    return string_em_minuscula


#  ainda nao utlizado
def contar_linhas_de_um_arquivo(endereco, formato):
    arquivo = open(f"{endereco}.{formato}", "r")
    separando_em_linhas = arquivo.readlines()
    total_linhas = len(separando_em_linhas)
    return total_linhas
