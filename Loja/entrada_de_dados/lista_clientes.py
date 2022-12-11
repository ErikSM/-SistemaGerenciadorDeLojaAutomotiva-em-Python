from estrutura.Cliente import Cliente

clientes_registrados = list()


def add_cliente_em_lista(cliente: Cliente, variavel, cnpj_loja_vinculada):
    cliente.nome_da_variavel = variavel
    cliente.cnpj_loja = cnpj_loja_vinculada
    clientes_registrados.append(cliente)
    _atualizar_contador_da_lista()


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in clientes_registrados:
        i.posicao_na_lista = ""
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


# ------------  --------------    ------------  ---------------   --------


nome = "Erik Miyajima"
cpf = "23948729487"
telefone = "7539579"
email = "sjfojfo@com"
cliente_erik_miyajima23948729487 = Cliente(nome, cpf, telefone, email)
add_cliente_em_lista(cliente_erik_miyajima23948729487, "cliente_erik_miyajima23948729487", 124134100000)


nome = "Ayumi Mello"    
cpf = "32489765098"    
telefone = "990834562345"    
email = "ayu@hotmail.com"    
cliente_ayumi_mello32489765098 = Cliente(nome, cpf, telefone, email)
add_cliente_em_lista(cliente_ayumi_mello32489765098, "cliente_ayumi_mello32489765098", 124134100000)


nome = "Joao Firmino"    
cpf = "99087678990"    
telefone = "889977665478"    
email = "jfno@hotmail.com"    
cliente_joao_firmino99087678990 = Cliente(nome, cpf, telefone, email)
add_cliente_em_lista(cliente_joao_firmino99087678990, "cliente_joao_firmino99087678990", 124134100000)

