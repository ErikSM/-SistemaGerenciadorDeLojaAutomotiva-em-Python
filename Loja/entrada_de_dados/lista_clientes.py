from estrutura.Cliente import Cliente


clientes_registrados = list()
codigos_de_clientes_existentes = list()


def add_cliente_em_lista(cliente: Cliente, variavel, cnpj_loja_vinculada, linha_no_arquivo):
    cliente.nome_da_variavel = variavel
    cliente.cnpj_loja = cnpj_loja_vinculada
    cliente.linha_no_arquivo = linha_no_arquivo
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
cpf = "52998224725"
telefone = "7539579"
email = "sjfojfo@com"
codigo = "251752"
cliente_251752 = Cliente(nome, cpf, telefone, email, codigo)
add_cliente_em_lista(cliente_251752, "cliente_251752 ", 124134100000, 33)


nome = "Ayumi Mello"
cpf = "52998224725"
telefone = "990834562345"
email = "ayu@hotmail.com"
codigo = "749240"
cliente_749240 = Cliente(nome, cpf, telefone, email, codigo)
add_cliente_em_lista(cliente_749240, "cliente_749240", 124134100000, 42)


nome = "Fernanda Lopez"
cpf = "52998224725"
telefone = "990830582388"
email = "ferlo@gmail.com"
codigo = "417257"
cliente_417257 = Cliente(nome, cpf, telefone, email, codigo)
add_cliente_em_lista(cliente_417257, "cliente_417257", 124134100000, 51)

