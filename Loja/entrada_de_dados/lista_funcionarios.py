from estrutura.Funcionario import Funcionario


funcionarios_registrados = list()
codigos_de_funcionarios_existentes = list()


def add_funcionario_na_lista(funcionario: Funcionario, cnpj_loja_vinculada, linha_no_arquivo):
    funcionario.cnpj_loja = cnpj_loja_vinculada
    funcionario.linha_no_arquivo = linha_no_arquivo
    funcionario.preencher_cargos_e_salarios()
    funcionario.nome_da_variavel = f"funcionario_{funcionario.codigo}"
    funcionarios_registrados.append(funcionario)
    _atualizar_contador_da_lista()
    _add_novo_codigo_na_lista_de_codigos_ja_existentes(funcionario.codigo)


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in funcionarios_registrados:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo):
    codigo_int = int(codigo)
    codigos_de_funcionarios_existentes.append(codigo_int)


# -----------------  -------------------  ------------------  ------------------


nome = "Joao Pereira"
cpf = "52998224725"
telefone = "909876567898"
email = "jpere@gmail.com"
codigo = "267707"
cargo = "gerente"
funcionario_267707 = Funcionario(nome, cpf, telefone, email, codigo, cargo)
add_funcionario_na_lista(funcionario_267707, 124134100000, 34)


nome = "Armando Silveira"
cpf = "52998224725"
telefone = "998876673232"
email = "arman@gmail.com"
codigo = "379018"
cargo = "vendedor"
funcionario_379018 = Funcionario(nome, cpf, telefone, email, codigo, cargo)
add_funcionario_na_lista(funcionario_379018, 124134100000, 44)


nome = "Ana Julia"
cpf = "52998224725"
telefone = "889923487634"
email = "anaj@outlook.com"
codigo = "984713"
cargo = "secretaria"
funcionario_984713 = Funcionario(nome, cpf, telefone, email, codigo, cargo)
add_funcionario_na_lista(funcionario_984713, 124134100000, 54)


nome = "Edson Arantes"
cpf = "52998224725"
telefone = "888866663321"
email = "edara@hotmail.com"
codigo = "46643"
cargo = "zelador"
funcionario_46643 = Funcionario(nome, cpf, telefone, email, codigo, cargo)
add_funcionario_na_lista(funcionario_46643, 124134100000, 64)


nome = "Fernanda Silva"
cpf = "52998224725"
telefone = "998866663445"
email = "fesilva@hotmail.com"
codigo = "367715"
cargo = "advogado"
funcionario_367715 = Funcionario(nome, cpf, telefone, email, codigo, cargo)
add_funcionario_na_lista(funcionario_367715, 124134100000, 74)

