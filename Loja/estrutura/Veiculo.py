from abc import ABC, abstractmethod


class Veiculo(ABC):  # Classe Abstrata

    def __init__(self, montadora, nome, ano, valor_de_aquisicao, codigo):
        self.__montadora = montadora
        self.__nome = nome
        self.__ano = ano
        self.__valor_de_aquisicao = valor_de_aquisicao
        self.__codigo = codigo

        self.posicao_na_lista = " "
        self.nome_da_variavel = " "
        self.codigo_de_venda = " "

    def mostrar_atributos_principais(self):
        return f'\nmontadora = "{self.__montadora}"    \n' \
               f'nome = "{self.__nome}"    \n' \
               f'ano = "{self.__ano}"    \n' \
               f'valor_de_aquisicao = "{self.__valor_de_aquisicao}"    \n' \
               f'codigo_de_registro = "{self.__codigo}"    \n'

    @abstractmethod
    def abstractmethod(self):
        pass

    @property
    def montadora(self):
        return self.__montadora

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @property
    def valor_de_aquisicao(self):
        return self.__valor_de_aquisicao

    @valor_de_aquisicao.setter
    def valor_de_aquisicao(self, valor_de_aquisicao):
        self.__valor_de_aquisicao = valor_de_aquisicao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def loja_de_registro(self):
        return self.__loja_de_registro

    @loja_de_registro.setter
    def loja_de_registro(self, loja_de_registro):
        self.__loja_de_registro = loja_de_registro
