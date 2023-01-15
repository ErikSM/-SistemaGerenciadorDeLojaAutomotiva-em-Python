from testes.escrever_em_arquivo import texto_para_escrever_em_arquivo, elaborar_modificacao_em_arquivo


def modificar_arquivo():
    escrito = texto_para_escrever_em_arquivo()

    elaborar_modificacao_em_arquivo(escrito)


modificar_arquivo()