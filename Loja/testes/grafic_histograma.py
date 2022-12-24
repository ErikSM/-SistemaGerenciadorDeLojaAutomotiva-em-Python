import matplotlib.pyplot as plt

x = [2000, 3000, 1000, 2000, 2000, 3000]

y = [1, 2, 3, 4, 5, 6]
nomes = ["carlos", "alberto", "luiz", "carlos", "luiz", "carlos"]

plt.yticks(y, nomes)

plt.hist(x, y, figsize=(10, 6))

plt.title("histograma")
plt.show()
