import matplotlib.pyplot as plt

# realidade
x = [11, 15, 20, 30, 40, 50, 55]
y = [15, 40, 75, 90, 100, 105, 115]

# expectativa
x2 = [12, 17, 28, 31, 40, 56, 60]
y2 = [15, 16, 75, 90, 100, 115, 119]


# grafico de linhas(vermelho)
plt.plot(x, y, linestyle="-", color="red", marker=".", linewidth=1.0)
# grafico de dispersao(verde)
plt.scatter(x2, y2, color="green", marker="*", linewidths=3.0)


plt.style.use('ggplot')


plt.title("Linhas e Dispersao")
plt.xlabel("Eixo (X)", color="red", font="Consolas", size=20)
plt.ylabel("Eixo (Y)")
plt.show()
