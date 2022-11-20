from estrutura.Funcionario import Funcionario

funcionarios_registrados = list()


def add_funcionario_na_lista_do_main(funcionario: Funcionario, variavel):
    funcionario.nome_da_variavel = variavel
    funcionarios_registrados.append(funcionario)
    _atualizar_contador_da_lista()


def _atualizar_contador_da_lista():
    variavel_contador_de_posicao_na_lista = 0
    for i in funcionarios_registrados:
        i.posicao_na_lista = " "
        i.posicao_na_lista = variavel_contador_de_posicao_na_lista
        variavel_contador_de_posicao_na_lista += 1

# -----------------  -------------------  ------------------  ------------------


nome = "Joao Silva"
cpf = "98476538927"
telefone = "29857298798"
email = "joao@.com"
cargo = "gerente"
funcionario_joao_silva98476538927 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_joao_silva98476538927,
                                 "funcionario_joao_silva98476538927")


nome = "Maria Souza"
cpf = "8973542"
telefone = "9923424"
email = "ma@.com"
cargo = "vendedor"
funcionario_maria_souza8973542 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_maria_souza8973542,
                                 "funcionario_maria_souza8973542")


nome = "Jorge Monteiro"
cpf = "9872984729"
telefone = "9988234252"
email = "jor@.com"
cargo = "vendedor"
funcionario_jorge_monteiro9872984729 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_jorge_monteiro9872984729, "funcionario_jorge_monteiro9872984729")


nome = "Mariana Silveira"
cpf = "98759827489"
telefone = "8899944342"
email = "mariii@com"
cargo = "secretaria"
funcionario_mariana_silveira98759827489 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_mariana_silveira98759827489, "funcionario_mariana_silveira98759827489")


nome = "Batista Melo"
cpf = "2384728974"
telefone = "77788882341"
email = "bast@com"
cargo = "vendedor"
funcionario_batista_melo2384728974 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_batista_melo2384728974, "funcionario_batista_melo2384728974")


nome = "Fabiana Junqueira"
cpf = "987987"
telefone = "888992342"
email = "fabiju@com"
cargo = "vendedor"
funcionario_fabiana_junqueira987987 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_fabiana_junqueira987987, "funcionario_fabiana_junqueira987987")
