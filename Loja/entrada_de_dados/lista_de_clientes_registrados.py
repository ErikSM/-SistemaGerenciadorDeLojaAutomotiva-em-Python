from estrutura.Cliente import Cliente

clientes_registrados = list()

variavel_contador_de_posicao_na_lista = 0


def add_cliente_na_lista_do_main(cliente: Cliente, posicao):
    cliente.posicao_na_lista = posicao
    clientes_registrados.append(cliente)


# ------------  --------------    ------------  ---------------   --------


nome = "Erik Satoshi"
cpf = "22233344460"
telefone = "243425425"
email = "erik@hot.com"
cliente_Erik_Satoshi22233344460 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_Erik_Satoshi22233344460, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

nome = "Joao Batista"
cpf = "827492749"
telefone = "8798739"
email = "ecoo@hsid.com"
cliente_Joao_Batista827492749 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_Joao_Batista827492749, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

