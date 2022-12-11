import tkinter

from estrutura import Loja


def organizar_ranking_de_carros_mais_vendidos_da_loja(loja: Loja):
    lista_de_ordem_rankiado = list()

    carros_mais_vendidos = dict()
    quantidade = 1

    texto_temporario = tkinter.Text()
    texto_temporario.insert(1.0, "\n      ((RAnking de venda))\n\n\n")

    # definindo quantidade
    for venda in loja.dicionario_da_loja["vendas"]:
        if venda.veiculo.nome in carros_mais_vendidos:
            carros_mais_vendidos[venda.veiculo.nome] = carros_mais_vendidos[venda.veiculo.nome] + 1
        else:
            carros_mais_vendidos[venda.veiculo.nome] = quantidade

    # ordenando ranking
    for carro in carros_mais_vendidos:
        lista_de_ordem_rankiado.append(f'Quantidade: {carros_mais_vendidos[carro]}  -  Carro: {carro}')
    lista_de_ordem_rankiado.sort()
    lista_de_ordem_rankiado.reverse()

    # escrevendo relatorio
    for i in lista_de_ordem_rankiado:
        texto_temporario.insert("end", f'{i}\n')

    return texto_temporario.get(1.0, "end")


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






