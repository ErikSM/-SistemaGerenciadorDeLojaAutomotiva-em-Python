from estrutura.Cliente import Cliente

clientes_registrados = list()

variavel_contador_de_posicao_na_lista = 0


def add_cliente_na_lista_do_main(cliente: Cliente, posicao, variavel):
    cliente.posicao_na_lista = posicao
    cliente.nome_da_variavel = variavel
    clientes_registrados.append(cliente)


# ------------  --------------    ------------  ---------------   --------


nome = "Erik Miyajima"
cpf = "897498274"
telefone = "09923847"
email = "erikj@.com"
cliente_erik_miyajima897498274 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_erik_miyajima897498274, variavel_contador_de_posicao_na_lista, "cliente_erik_miyajima897498274")
variavel_contador_de_posicao_na_lista += 1


nome = "Ayumi Souza"
cpf = "234299"
telefone = "9097645654"
email = "ayu@.com"
cliente_ayumi_souza234299 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_ayumi_souza234299, variavel_contador_de_posicao_na_lista, "cliente_ayumi_souza234299")
variavel_contador_de_posicao_na_lista += 1

