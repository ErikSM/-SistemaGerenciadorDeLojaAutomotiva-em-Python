class Funcionario:

    def __init__(self, nome, cpf, telefone, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

        self.salario = None
        self.cargo = None

        self.posicao_na_lista = " "
        self.nome_da_variavel = " "

    def mostrar_dados_do_cliente(self):
        return f'\nFuncionario = "{self.__nome}"    \n' \
               f'cpf = "{self.__cpf}"    \n' \
               f'telefone = "{self.__telefone}"    \n' \
               f'email = "{self.__email}"    \n'

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

