from entrada_de_dados.lista_vendas import vendas_registradas

carros_mais_vendidos = dict()
contador = 1

for i in vendas_registradas:
    if i.veiculo.nome in carros_mais_vendidos:
        carros_mais_vendidos[i.veiculo.nome] = carros_mais_vendidos[i.veiculo.nome] + 1
    else:
        carros_mais_vendidos[i.veiculo.nome] = contador

print(carros_mais_vendidos)

for i in carros_mais_vendidos:
    print(f"{i}:{carros_mais_vendidos[i]}")

ordenado = sorted(carros_mais_vendidos.items(), key=lambda item: item[1])
ordenado.reverse()

print(ordenado)
