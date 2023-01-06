import matplotlib.pyplot as plt


def construir_grafico_barras(dicionario, x_nome, y_nome, grafico_nome, definicao_mascara_y=""):
    plt.figure(figsize=(10, 6), facecolor='grey')
    plt.axes().set_facecolor('grey')
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

    listax = list()
    listay = list()
    for i in dicionario:
        listax.append(i)
        listay.append(dicionario[i])

    if len(dicionario) > 3:
        plt.bar(listax, listay, align="center", facecolor="black", width=0.3)

    elif len(dicionario) > 5:
        plt.bar(listax, listay, align="center", facecolor="black", width=0.1)

    else:
        plt.bar(listax, listay, align="center", facecolor="black", width=0.5)

    plt.title("{}".format(grafico_nome), font="Times New Roman", color="black", fontsize=25)
    plt.xlabel("{}".format(x_nome), font="Consolas", color="red", fontsize=14)
    plt.ylabel("{} {}".format(y_nome, definicao_mascara_y), font="Consolas", color="red", fontsize=14)

    plt.show()


def construir_grafico_linhas(dicionario, x_nome, y_nome, grafico_nome, definicao_mascara_y=None):
    plt.figure(figsize=(10, 6), facecolor='grey')
    plt.axes().set_facecolor('grey')
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

    listax = list()
    listay = list()
    for i in dicionario:
        listax.append(i)
        listay.append(dicionario[i])

    plt.plot(listax, listay, linestyle="-", color="black", marker=".", linewidth=1.0)

    plt.title("{}".format(grafico_nome), font="Times New Roman", color="red", fontsize=20)
    plt.xlabel("{}".format(x_nome), font="Consolas", color="black", fontsize=14)
    plt.ylabel("{} {}".format(y_nome, definicao_mascara_y), font="Consolas", color="black", fontsize=14)

    plt.show()
