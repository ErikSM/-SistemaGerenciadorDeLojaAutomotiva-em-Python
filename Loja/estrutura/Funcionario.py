from admin import cargos_e_salarios

'''
    classe em construcao
'''


class Funcionario:

    def __init__(self, nome, cpf, telefone, email, cargo):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

        self.__cargo = cargos_e_salarios.dicio_de_cargos[cargo]
        self.__salario = self.__cargo["salario"]
        self.bonus = self.__cargo["bonus"]
        self.comissao = self.__cargo["comissao"]

        self.__bonus = None
        self.__comissao = None

        self.posicao_na_lista = " "
        self.nome_da_variavel = " "

    def mostrar_dados_do_funcionario(self):
        return f'\nFuncionario = "{self.__nome}"    \n' \
               f'cpf = "{self.__cpf}"    \n' \
               f'telefone = "{self.__telefone}"    \n' \
               f'email = "{self.__email}"    \n' \
               f'cargo = "{self.__cargo["funcao"]}"    \n' \
               f'salario = "{self.__salario}"    '

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo


