from estrutura.Cliente import Cliente

clientes_registrados = list()

variavel_contador_de_posicao_na_lista = 0


def add_cliente_na_lista_do_main(cliente: Cliente, posicao, variavel):
    cliente.posicao_na_lista = posicao
    cliente.nome_da_variavel = variavel
    clientes_registrados.append(cliente)


# ------------  --------------    ------------  ---------------   --------


nome = "Erik Miyajima"
cpf = "23434248979"
telefone = "989234242"
email = "erik@.com"
cliente_erik_miyajima23434248979 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_erik_miyajima23434248979, variavel_contador_de_posicao_na_lista, "cliente_erik_miyajima23434248979")
variavel_contador_de_posicao_na_lista += 1


nome = "Ayumi Souza"
cpf = "98798798"
telefone = "234234234"
email = "ayu@.com"
cliente_ayumi_souza98798798 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_ayumi_souza98798798, variavel_contador_de_posicao_na_lista, "cliente_ayumi_souza98798798")
variavel_contador_de_posicao_na_lista += 1

