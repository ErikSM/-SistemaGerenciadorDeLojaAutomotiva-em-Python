from estrutura.Funcionario import Funcionario


funcionarios_registrados = list()
codigos_de_funcionarios_existentes = list()


def add_funcionario_na_lista(funcionario: Funcionario, cnpj_loja, linha):
    funcionario.cnpj_loja = cnpj_loja
    funcionario.linha_no_arquivo = linha
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


def _add_novo_codigo_na_lista_de_codigos_ja_existentes(codigo_novo):
    codigo_int = int(codigo_novo)
    codigos_de_funcionarios_existentes.append(codigo_int)


# -----------------  -------------------  ------------------  ------------------


nome = "Joao Pereira"
cpf = "52998224725"
telefone = "909876567898"
email = "jpere@gmail.com"
codigo = "267707"
funcionario_267707 = Funcionario(nome, cpf, telefone, email, codigo)
funcionario_267707.cargo = "gerente"
add_funcionario_na_lista(funcionario_267707, 43217051000182, 37)


nome = "Armando Silveira"
cpf = "46094627024"
telefone = "998876673232"
email = "arman@gmail.com"
codigo = "379018"
funcionario_379018 = Funcionario(nome, cpf, telefone, email, codigo)
funcionario_379018.cargo = "vendedor"
add_funcionario_na_lista(funcionario_379018, 43217051000182, 47)


nome = "Ana Julia"
cpf = "51974602028"
telefone = "889923487634"
email = "anaj@outlook.com"
codigo = "984713"
funcionario_984713 = Funcionario(nome, cpf, telefone, email, codigo)
funcionario_984713.cargo = "secretaria"
add_funcionario_na_lista(funcionario_984713, 43217051000182, 57)


nome = "Edson Arantes"
cpf = "93120811017"
telefone = "888866663321"
email = "edara@hotmail.com"
codigo = "46643"
funcionario_46643 = Funcionario(nome, cpf, telefone, email, codigo)
funcionario_46643.cargo = "zelador"
add_funcionario_na_lista(funcionario_46643, 43217051000182, 67)


nome = "Fernanda Silva"
cpf = "31619128020"
telefone = "998866663445"
email = "fesilva@hotmail.com"
codigo = "367715"
funcionario_367715 = Funcionario(nome, cpf, telefone, email, codigo)
funcionario_367715.cargo = "advogado"
add_funcionario_na_lista(funcionario_367715, 43217051000182, 77)


nome = "Joao Batista"    
cpf = "60433627085"
telefone = "978874673232"    
email = "joaob@gmail.com"    
codigo = "633018"    
funcionario_633018 = Funcionario(nome, cpf, telefone, email, codigo)
funcionario_633018.cargo = "vendedor"
add_funcionario_na_lista(funcionario_633018, 43217051000182, 87)

