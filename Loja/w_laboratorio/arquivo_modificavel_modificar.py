from w_laboratorio.arquivo_modificavel_escrever import texto_para_escrever_em_arquivo, elaborar_modificacao_em_arquivo


def modificar_arquivo():
    escrito = texto_para_escrever_em_arquivo()

    elaborar_modificacao_em_arquivo(escrito)


modificar_arquivo()