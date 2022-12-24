import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [2000.00, 3000.00, 4000.00]

faixa = ["18-30", "31-60", "61-90"]

plt.xticks(x, faixa)
plt.bar(x, y, align="center")



plt.title("Barras")
plt.xlabel("Idade(X)")
plt.ylabel("Renda(Y)")
plt.show()
