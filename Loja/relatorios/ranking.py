import tkinter

from relatorios.graficos import construir_grafico_barras
from estrutura import Loja


def organizar_rankings_da_loja(loja: Loja, lista_analisada):
    carros_mais_vendidos = dict()
    melhores_clientes = dict()

    ranking_dos_carros = list()
    ranking_dos_clientes = list()

    texto_temporario = tkinter.Text()
    primeira_venda = 1

    # definindo quantidade
    for i in loja.dicionario_da_loja["vendas"]:
        if i.veiculo.nome in carros_mais_vendidos:
            carros_mais_vendidos[i.veiculo.nome] = carros_mais_vendidos[i.veiculo.nome] + 1
        else:
            carros_mais_vendidos[i.veiculo.nome] = primeira_venda

        if i.cliente.nome in melhores_clientes:
            melhores_clientes[i.cliente.nome] = melhores_clientes[i.cliente.nome] + 1
        else:
            melhores_clientes[i.cliente.nome] = primeira_venda

    # ordenando ranking
    for i in carros_mais_vendidos:
        ranking_dos_carros.append(f'Quantidade de vendas: {carros_mais_vendidos[i]}  -  Carro: {i}')
    ranking_dos_carros.sort()
    ranking_dos_carros.reverse()

    for i in melhores_clientes:
        ranking_dos_clientes.append(f'Total de Compras: {melhores_clientes[i]}  -  Cliente: {i}')
    ranking_dos_clientes.sort()
    ranking_dos_clientes.reverse()

    # escrevendo relatorio
    for i in ranking_dos_carros:
        texto_temporario.insert("end", f'{i}\n')
    texto_temporario.insert(1.0, "\n       ((Ranking de Carros))\n\n\n")
    string_ranking_de_carros = texto_temporario.get(1.0, "end")
    texto_temporario.delete(1.0, "end")

    for i in ranking_dos_clientes:
        texto_temporario.insert("end", f'{i}\n')
    texto_temporario.insert(1.0, "\n       ((Ranking de Clientes))\n\n\n")
    string_ranking_de_clientes = texto_temporario.get(1.0, "end")
    texto_temporario.delete(1.0, "end")

    # mostrando grafico e imprimindo resultado
    if lista_analisada == "carros":
        definicoes_do_grafico = ("Modelos", "Quantidade de vendas", "Mais vendidos")
        construir_grafico_barras(carros_mais_vendidos, definicoes_do_grafico)

        return string_ranking_de_carros

    elif lista_analisada == "clientes":
        definicoes_do_grafico = ("clientes", "Quantidade de compras", "Melhores clientes")
        construir_grafico_barras(melhores_clientes, definicoes_do_grafico)

        return string_ranking_de_clientes
