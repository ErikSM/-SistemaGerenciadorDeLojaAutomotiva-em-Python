
import tkinter


def elaborar_modificacao_em_arquivo(escrever):
    texto_temporario = tkinter.Text()

    arquivo = open(f"../relatorios/arquivo_modificavel.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = escrever

    file = open(f"../relatorios/arquivo_modificavel.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()


def texto_para_escrever_em_arquivo():
    return f'\n' \
           f'# teste    \n' \
           f'nome = "cargo"    \n' \
           f'sarario = "$$"    \n' \
           f'bonus = "%"    \n' \
           f'comissao = "%"   \n' \
           f'cnpj = "xxx"    \n' \
           f'linha = "x"    \n' \
           f''
