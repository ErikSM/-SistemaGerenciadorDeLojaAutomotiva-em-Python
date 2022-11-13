from estrutura.Cliente import Cliente

clientes_registrados = list()


def add_cliente_na_lista_do_main(cliente: Cliente, variavel):
    cliente.nome_da_variavel = variavel
    clientes_registrados.append(cliente)
    _atualizar_contador_da_lista()


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in clientes_registrados:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


# ------------  --------------    ------------  ---------------   --------


nome = "Erik Miyajima"
cpf = "23434248979"
telefone = "989234242"
email = "erik@.com"
cliente_erik_miyajima23434248979 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_erik_miyajima23434248979, "cliente_erik_miyajima23434248979")


nome = "Ayumi Souza"
cpf = "98798798"
telefone = "234234234"
email = "ayu@.com"
cliente_ayumi_souza98798798 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_ayumi_souza98798798, "cliente_ayumi_souza98798798")


nome = "jose Silveira"
cpf = "787979242"
telefone = "9977000222"
email = "jsil@com"
cliente_jose_silveira787979242 = Cliente(nome, cpf, telefone, email)
add_cliente_na_lista_do_main(cliente_jose_silveira787979242,"cliente_jose_silveira787979242")

