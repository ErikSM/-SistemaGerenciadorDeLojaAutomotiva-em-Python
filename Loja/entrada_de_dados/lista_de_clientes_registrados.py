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

nome = "Maria da Silva"
cpf = "234235"
telefone = "345345"
email = "sef@.com"
cliente_Maria_da_Silva234235 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_Maria_da_Silva234235, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

nome = "Fabielle Souza"
cpf = "234223435"
telefone = "345345"
email = "sef@.com"
cliente_Fabielle_Souza234223435 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_Fabielle_Souza234223435, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

nome = "Fabiana das Neves"
cpf = "24"
telefone = "3543"
email = "dss@.com"
cliente_Fabiana_da_Neves24 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_Fabiana_da_Neves24, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

nome = "Ayumi Barbara"
cpf = "8768687"
telefone = "090876876"
email = "ayumi@xx.com"
cliente_Ayumi_Barbara8768687 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_Ayumi_Barbara8768687, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

nome = "Gloria da Silva"
cpf = "25452"
telefone = "235242"
email = "dfssf@com"
cliente_gloria_da_silva25452 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_gloria_da_silva25452, variavel_contador_de_posicao_na_lista)
variavel_contador_de_posicao_na_lista += 1

