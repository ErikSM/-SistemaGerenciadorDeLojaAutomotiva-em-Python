from estrutura.Funcionario import Funcionario

funcionarios_registrados = list()


def add_funcionario_na_lista(funcionario: Funcionario, variavel, cnpj_loja_vinculada, linha_no_arquivo):
    funcionario.nome_da_variavel = variavel
    funcionario.cnpj_loja = cnpj_loja_vinculada
    funcionario.linha_no_arquivo = linha_no_arquivo
    funcionarios_registrados.append(funcionario)
    _atualizar_contador_da_lista()


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in funcionarios_registrados:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1


# -----------------  -------------------  ------------------  ------------------


nome = "Joao Pereira"
cpf = "77832209823"
telefone = "909876567898"
email = "jpere@gmail.com"
cargo = "gerente"
funcionario_joao_pereira77832209823 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista(funcionario_joao_pereira77832209823,
                         "funcionario_joao_pereira77832209823", 124134100000, 25)


nome = 'Joana Aparecida'
cpf = "98767823490"
telefone = "889923487634"
email = "anaj@outlook.com"
cargo = "secretaria"
funcionario_ana_julia98767823490 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista(funcionario_ana_julia98767823490,
                         "funcionario_ana_julia98767823490", 124134100000, 35)


nome = "Astolfo Formiga"
cpf = "87654678990"
telefone = "888866663333"
email = "asfo@hotmail.com"
cargo = "zelador"
funcionario_astolfo_formiga87654678990 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista(funcionario_astolfo_formiga87654678990,
                         "funcionario_astolfo_formiga87654678990", 124134100000, 45)



