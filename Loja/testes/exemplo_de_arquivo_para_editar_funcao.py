import tkinter


def editar_arquivo():
    texto_temporario = tkinter.Text()

    arquivo = open("exemplo_de_arquivo_para_editar.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = "nome = 'Joana Aparecida'"

    file = open("exemplo_de_arquivo_para_editar.py", "w")

    texto_temporario.delete(35.0, 35.99)
    texto_temporario.insert(35.0, arquivo_escrito)

    file.write(texto_temporario.get(1.0, "end"))

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


editar_arquivo()