import matplotlib.pyplot as plt


def construir_grafico_barras(dicionario, definicoes: tuple, definicao_mascara_y=""):

    x_nome, y_nome, grafico_nome = definicoes[0], definicoes[1], definicoes[2]

    plt.figure(figsize=(10, 6), facecolor='#273A3F')
    plt.axes().set_facecolor('#273A3F')
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

    listax = list()
    listay = list()
    for i in dicionario:
        listax.append(i)
        listay.append(dicionario[i])

    if len(dicionario) > 3:
        plt.bar(listax, listay, align="center", facecolor="#01191F", width=0.3)

    elif len(dicionario) > 5:
        plt.bar(listax, listay, align="center", facecolor="#01191F", width=0.1)

    else:
        plt.bar(listax, listay, align="center", facecolor="#01191F", width=0.5)

    plt.title("{}".format(grafico_nome), font="Times New Roman", color="#01191F", fontsize=25)
    plt.xlabel("{}".format(x_nome), font="Consolas", color="#34514F", fontsize=14)
    plt.ylabel("{} {}".format(y_nome, definicao_mascara_y), font="Consolas", color="#34514F", fontsize=14)

    plt.show()


def construir_grafico_linhas(dicionario, definicoes: tuple, definicao_mascara_y=None):

    x_nome, y_nome, grafico_nome = definicoes[0], definicoes[1], definicoes[2]

    plt.figure(figsize=(10, 6), facecolor='#273A3F')
    plt.axes().set_facecolor('#273A3F')
    plt.tick_params(axis='x', labelsize=8)
    plt.tick_params(axis='y', labelsize=8)

    listax = list()
    listay = list()
    for i in dicionario:
        listax.append(i)
        listay.append(dicionario[i])

    plt.plot(listax, listay, linestyle="-", color="#01191F", marker=".", linewidth=1.0)

    plt.title("{}".format(grafico_nome), font="Times New Roman", color="#34514F", fontsize=20)
    plt.xlabel("{}".format(x_nome), font="Consolas", color="#01191F", fontsize=14)
    plt.ylabel("{} {}".format(y_nome, definicao_mascara_y), font="Consolas", color="#01191F", fontsize=14)

    plt.show()
