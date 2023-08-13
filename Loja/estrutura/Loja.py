
from entrada_de_dados.validar_documento import Documento
from entrada_de_dados.validar_telefone import Telefone


class Loja:

    def __init__(self, nome, cnpj, telefone, email, codigo):

        self.__nome = nome
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.__email = email
        self.__codigo = codigo

        self.__senha = None

        self.posicao_na_lista = None
        self.nome_da_variavel = " "

        self.dicionario_da_loja = dict()

        self.dicionario_da_loja["carros"] = self.carros_registrados = list()
        self.dicionario_da_loja["clientes"] = self.clientes_registrados = list()
        self.dicionario_da_loja["funcionarios"] = self.funcionarios_registrados = list()
        self.dicionario_da_loja["vendas"] = self.vendas_registradas = list()

    def __str__(self):
        return f'\nloja = "{self.__nome}"   \n' \
               f'cnpj = "{self.__cnpj}"   \n' \
               f'contato = "{self.__telefone}"   \n'

    def mostrar_dados(self):
        return f'\nloja:{self.__nome}   \n' \
               f'cnpj:{Documento(self.__cnpj)}   \n' \
               f'contato:{Telefone(self.__telefone)}   \n'

    def adicionar_carro(self, carro):
        self.carros_registrados.append(carro)

    def adicionar_cliente(self, cliente):
        self.clientes_registrados.append(cliente)

    def adicionar_funcionario(self, funcionario):
        self.funcionarios_registrados.append(funcionario)

    def adicionar_venda(self, venda):
        self.vendas_registradas.append(venda)

    @property
    def nome(self):
        return self.__nome

    @property
    def cnpj(self):
        return self.__cnpj

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

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

