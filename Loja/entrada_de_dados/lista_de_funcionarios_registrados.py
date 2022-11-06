from estrutura.Funcionario import Funcionario

funcionarios_registrados = list()

variavel_contador_de_posicao_na_lista = 0


''' 
Ainda em desenvolvimento

'''


def add_funcionario_na_lista_do_main(funcionario: Funcionario, posicao, variavel):
    funcionario.posicao_na_lista = posicao
    funcionario.nome_da_variavel = variavel
    funcionarios_registrados.append(funcionario)

# -----------------  -------------------  ------------------  ------------------


nome = "Joao Silva"
cpf = "98476538927"
telefone = "29857298798"
email = "joao@.com"
cargo = "gerente"
funcionario_joao_silva98476538927 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_joao_silva98476538927, variavel_contador_de_posicao_na_lista,
                                 "funcionario_joao_silva98476538927")
variavel_contador_de_posicao_na_lista += 1


nome = "Maria Souza"
cpf = "8973542"
telefone = "9923424"
email = "ma@.com"
cargo = "vendedor"
funcionario_maria_souza8973542 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_maria_souza8973542, variavel_contador_de_posicao_na_lista,
                                 "funcionario_maria_souza8973542")
variavel_contador_de_posicao_na_lista += 1


nome = "Jorge Monteiro"
cpf = "234242897"
telefone = "998833322"
email = "jo@com"
cargo = "vendedor"
funcionario_jorge_monteiro234242897 = Funcionario(nome, cpf, telefone, email, cargo)
add_funcionario_na_lista_do_main(funcionario_jorge_monteiro234242897, variavel_contador_de_posicao_na_lista, "funcionario_jorge_monteiro234242897")
variavel_contador_de_posicao_na_lista += 1

