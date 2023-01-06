from entrada_de_dados.validar_documento import mascarar_cpf
from entrada_de_dados.validar_telefone import Telefone


class Cliente:

    def __init__(self, nome, cpf, telefone, email, codigo):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__codigo = codigo

        self.__cnpj_loja = None

        self.linha_no_arquivo = int()

        self.posicao_na_lista = " "
        self.nome_da_variavel = " "

    def mostrar_atributos_principais(self):
        return f'\nnome = "{self.__nome}"    \n' \
               f'cpf = "{self.__cpf}"    \n' \
               f'telefone = "{self.__telefone}"    \n' \
               f'email = "{self.__email}"    \n' \
               f'codigo = "{self.__codigo}"    \n'

    def mostrar_dados(self):
        return f'\nnome = "{self.__nome}"    \n' \
               f'cpf = "{mascarar_cpf(self.__cpf)}"    \n' \
               f'telefone = "{Telefone(self.__telefone)}"    \n' \
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

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cnpj_loja(self):
        return self.__cnpj_loja

    @cnpj_loja.setter
    def cnpj_loja(self, cnpj_loja):
        self.__cnpj_loja = cnpj_loja