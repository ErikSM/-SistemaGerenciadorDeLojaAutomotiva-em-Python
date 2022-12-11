import tkinter

from estrutura import Loja


def organizar_rankings_da_loja(loja: Loja, lista_analisada):
    carros_mais_vendidos = dict()
    melhores_clientes = dict()

    quantidade = 1

    lista_de_ranking_dos_carros = list()
    lista_de_ranking_dos_clientes = list()

    texto_temporario = tkinter.Text()

    # definindo quantidade
    for venda in loja.dicionario_da_loja["vendas"]:
        if venda.veiculo.nome in carros_mais_vendidos:
            carros_mais_vendidos[venda.veiculo.nome] = carros_mais_vendidos[venda.veiculo.nome] + 1
        else:
            carros_mais_vendidos[venda.veiculo.nome] = quantidade
        if venda.cliente.nome in melhores_clientes:
            melhores_clientes[venda.cliente.nome] = melhores_clientes[venda.cliente.nome] + 1
        else:
            melhores_clientes[venda.cliente.nome] = quantidade

    # ordenando ranking
    for carro in carros_mais_vendidos:
        lista_de_ranking_dos_carros.append(f'Quantidade de vendas do modelo: {carros_mais_vendidos[carro]}  -  Carro: {carro}')
    lista_de_ranking_dos_carros.sort()
    lista_de_ranking_dos_carros.reverse()
    for cliente in melhores_clientes:
        lista_de_ranking_dos_clientes.append(f'Total de Compras: {melhores_clientes[cliente]}  -  Cliente: {cliente}')
    lista_de_ranking_dos_clientes.sort()
    lista_de_ranking_dos_clientes.reverse()

    # escrevendo relatorio
    for i in lista_de_ranking_dos_carros:
        texto_temporario.insert("end", f'{i}\n')
    texto_temporario.insert(1.0, "\n       ((Ranking de Carros mais Vendidos))\n\n\n")
    string_ranking_de_carros = texto_temporario.get(1.0, "end")
    texto_temporario.delete(1.0, "end")

    for i in lista_de_ranking_dos_clientes:
        texto_temporario.insert("end", f'{i}\n')
    texto_temporario.insert(1.0, "\n       ((Ranking Melhores Clientes))\n\n\n")
    string_ranking_de_clientes = texto_temporario.get(1.0, "end")
    texto_temporario.delete(1.0, "end")

    if lista_analisada == "carros":
        return string_ranking_de_carros
    if lista_analisada == "clientes":
        return string_ranking_de_clientes




teste = '''
- Passo 1: criando um dicionario de quantidade com uma condicional que em caso de ja
haver a chave com algum determinado valor, ira adicionar a soma de +1 ao valor da chave
- Passo 2: criando uma lista que contem uma string que comeca com o valor do dicionario
criado e em seguida o nome do veiculo(String ja editada conforme o texto desejado no relatorio).
- Passo 3: ordenando a lista com a funcao sort() e em seguida invertendo a ordem para uma 
ordem decrescente com a funcao reverse()
- Passo 4: criando um laco "for" que imprime cada String da lista que ja esta na ordem desejada 
em uma linha por vez

'''






