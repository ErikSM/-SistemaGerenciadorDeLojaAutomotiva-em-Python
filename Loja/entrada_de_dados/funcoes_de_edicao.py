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


def tirar_espacos_e_maiusculas(string):
    string_espalhada = string.split()
    string_sem_espaco = "_".join(string_espalhada)
    string_em_minuscula = string_sem_espaco.lower()
    return string_em_minuscula
