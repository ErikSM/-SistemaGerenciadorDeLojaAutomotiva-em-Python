import tkinter

from entrada_de_dados.salvar_dados_adicionados_no_programa import atualizar_informacoes


def abrir_modificar_e_salvar_arquivo(endereco, escrever):
    texto_temporario = tkinter.Text()

    arquivo = open(f"{endereco}.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = escrever

    file = open(f"{endereco}.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()

