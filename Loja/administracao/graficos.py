import matplotlib.pyplot as plt

from entrada_de_dados.mascarar_preco import mascarar_preco


def construir_grafico_barras(dicionario, x_nome, y_nome, grafico_nome, definicao_mascara_y=None):
    listax = list()
    listay = list()
    for i in dicionario:
        listax.append(i)
        listay.append(dicionario[i])

    listay_mascarada = list()
    if definicao_mascara_y == "R$":
        for i in listay:
            listay_mascarada.append(mascarar_preco(i))
        plt.yticks(listay, listay_mascarada)

    plt.bar(listax, listay, align="center")

    plt.title("{}".format(grafico_nome))
    plt.xlabel("{}".format(x_nome))
    plt.ylabel("{}".format(y_nome))

    plt.show()
