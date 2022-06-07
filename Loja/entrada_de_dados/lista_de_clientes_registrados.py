from estrutura.Cliente import Cliente

clientes_registrados = list()

variavel_contador_de_posicao_na_lista = 0


def add_cliente_na_lista_do_main(cliente: Cliente, posicao, variavel):
    cliente.posicao_na_lista = posicao
    cliente.nome_da_variavel = variavel
    clientes_registrados.append(cliente)


# ------------  --------------    ------------  ---------------   --------


nome = "Erik Satoshi"
cpf = "22233344460"
telefone = "243425425"
email = "erik@hot.com"
cliente_Erik_Satoshi22233344460 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_Erik_Satoshi22233344460, variavel_contador_de_posicao_na_lista, "cliente_Erik_Satoshi22233344460")
variavel_contador_de_posicao_na_lista += 1


nome = "Ayumi Souza"
cpf = "2342"
telefone = "23232432"
email = "kljslf@.com"
cliente_ayumi_souza2342 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_ayumi_souza2342, variavel_contador_de_posicao_na_lista, "cliente_Erik_Satoshi22233344460")
variavel_contador_de_posicao_na_lista += 1


nome = "Aline Barros"
cpf = "23424"
telefone = "252342"
email = "dfsd@com"
cliente_aline_barros23424 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_aline_barros23424, variavel_contador_de_posicao_na_lista, "cliente_aline_barros23424")
variavel_contador_de_posicao_na_lista += 1


nome = "Joao Silva"
cpf = "352"
telefone = "90787987"
email = "sfwfs@com"
cliente_joao_silva352 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_joao_silva352, variavel_contador_de_posicao_na_lista, "cliente_joao_silva352")
variavel_contador_de_posicao_na_lista += 1

