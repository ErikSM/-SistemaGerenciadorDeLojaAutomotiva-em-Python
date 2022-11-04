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
funcionario_joao_silva98476538927 = Funcionario(nome, cpf, telefone, email)
add_funcionario_na_lista_do_main(funcionario_joao_silva98476538927, variavel_contador_de_posicao_na_lista, "funcionario_joao_silva98476538927")
variavel_contador_de_posicao_na_lista += 1

