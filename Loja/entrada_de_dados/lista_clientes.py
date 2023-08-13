from estrutura.Cliente import Cliente


clientes_registrados = list()
codigos_de_clientes_existentes = list()


def add_cliente_em_lista(cliente: Cliente, cnpj_loja_vinculada, linha_no_arquivo):
    cliente.cnpj_loja = cnpj_loja_vinculada
    cliente.linha_no_arquivo = linha_no_arquivo
    cliente.nome_da_variavel = f"cliente_{cliente.codigo}"
    clientes_registrados.append(cliente)

    _atualizar_contador_da_lista()
    _add_novo_codigo_na_lista_de_codigos_ja_existentes(cliente.codigo)


def _atualizar_contador_da_lista():

    variavel_contador_de_posicao_na_lista = 0

    for i in clientes_registrados:
        i.posicao_na_lista = ""
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo):
    codigo_int = int(codigo)
    codigos_de_clientes_existentes.append(codigo_int)


# ------------  --------------    ------------  ---------------   --------


nome = "Erik Miyajima"
cpf = "11247229041"
telefone = "7539579"
email = "sjfojfo@com"
codigo = "251752"
cliente_251752 = Cliente(nome, cpf, telefone, email, codigo)
add_cliente_em_lista(cliente_251752, 43217051000182, 36)


nome = "Ayumi Mello"
cpf = "75115194074"
telefone = "990834562345"
email = "ayu@hotmail.com"
codigo = "749240"
cliente_749240 = Cliente(nome, cpf, telefone, email, codigo)
add_cliente_em_lista(cliente_749240, 43217051000182, 45)


nome = "Fernanda Lopez"
cpf = "04906379060"
telefone = "990830582388"
email = "ferlo@gmail.com"
codigo = "417257"
cliente_417257 = Cliente(nome, cpf, telefone, email, codigo)
add_cliente_em_lista(cliente_417257, 43217051000182, 54)


nome = "Davi Jones"    
cpf = "63441223071"
telefone = "1234543456789"    
email = "haha@hotmail.com"    
codigo = "181819"    
cliente_181819 = Cliente(nome, cpf, telefone, email, codigo)
add_cliente_em_lista(cliente_181819, 43217051000182, 63)

