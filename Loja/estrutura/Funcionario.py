class Funcionario:

    def __init__(self, nome, cpf, salario, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        self.__senha = senha

    def __str__(self):
        return f'((Dados do funcionario:)):\n' \
               f'funcionario:{self.__nome}\n' \
               f'salario:{self.__salario}'

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
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def senha(self):
        pass

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

