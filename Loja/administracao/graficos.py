import matplotlib.pyplot as plt


def construir_grafico_barras(dicionario, x_nome, y_nome, grafico_nome, definicao_mascara_y=""):
    plt.figure(figsize=(10, 6), facecolor='grey')
    plt.axes().set_facecolor("grey")
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

    listax = list()
    listay = list()
    for i in dicionario:
        listax.append(i)
        listay.append(dicionario[i])

    plt.bar(listax, listay, align="center", facecolor="black")

    plt.title("{}".format(grafico_nome), font="Times New Roman", color="red", fontsize=20)
    plt.xlabel("{}".format(x_nome), font="Consolas", color="black", fontsize=14)
    plt.ylabel("{} {}".format(y_nome, definicao_mascara_y), font="Consolas", color="black", fontsize=14)

    plt.show()
