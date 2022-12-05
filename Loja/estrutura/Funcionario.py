from administracao import cargos_e_salarios
from entrada_de_dados.validar_documento import mascarar_cpf
from entrada_de_dados.validar_telefone import Telefone


class Funcionario:

    def __init__(self, nome, cpf, telefone, email, cargo):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

        self.__cnpj_loja = None

        self.__cargo = cargos_e_salarios.dicionario_de_cargos[cargo]
        self.__salario = self.__cargo["salario"]
        self.__bonus = self.__cargo["bonus"]
        self.__comissao = self.__cargo["comissao"]

        self.comissoes_recebidas = list()
        self.total_comissoes_recebidas = float()

        self.posicao_na_lista = " "
        self.nome_da_variavel = " "

    def mostrar_atributos_principais(self):
        return f'\nnome = "{self.__nome}"    \n' \
               f'cpf = "{self.__cpf}"    \n' \
               f'telefone = "{self.__telefone}"    \n' \
               f'email = "{self.__email}"    \n' \
               f'cargo = "{self.__cargo["cargo"]}"    \n'

    def mostrar_dados(self):
        return f'\nFuncionario = "{self.__nome}"    \n' \
               f'cpf = "{mascarar_cpf(self.__cpf)}"    \n' \
               f'telefone = "{Telefone(self.__telefone)}"    \n' \
               f'email = "{self.__email}"    \n' \
               f'cargo = "{self.__cargo["cargo"]}"    \n' \
               f'salario = "{self.__salario}"    \n' \
               f'bonus = "{int(self.__bonus * 100)}"%    \n' \
               f'comissao = "{int(self.__comissao * 100)}%" \n'

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
    def cnpj_loja(self):
        return self.__cnpj_loja

    @cnpj_loja.setter
    def cnpj_loja(self, cnpj_loja):
        self.__cnpj_loja = cnpj_loja

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao


