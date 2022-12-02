from estrutura.Funcionario import Funcionario

funcionarios_registrados = list()


def add_funcionario_na_lista(funcionario: Funcionario, variavel, cnpj_loja_vinculada):
    funcionario.nome_da_variavel = variavel
    funcionario.cnpj_loja = cnpj_loja_vinculada
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
                         "funcionario_joao_pereira77832209823", 124134100000)

nome = "Armando Silveira"
cpf = "88776540902"
telefone = "998876673232"
email = "arman@gmail.com"
cargo = "vendedor"
funcionario_armando_silveira88776540902 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista(funcionario_armando_silveira88776540902,
                         "funcionario_armando_silveira88776540902", 124134100000)


nome = "Ana Julia"    
cpf = "98767823490"    
telefone = "889923487634"    
email = "anaj@outlook.com"    
cargo = "secretaria"    
funcionario_ana_julia98767823490 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista(funcionario_ana_julia98767823490, 
                         "funcionario_ana_julia98767823490", 124134100000)

