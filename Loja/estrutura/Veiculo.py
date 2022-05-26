from abc import ABC, abstractmethod


class Veiculo(ABC):  # Classe Abstrata

    def __init__(self, montadora, nome, ano, valor_avaliado):
        self.__montadora = montadora
        self.__nome = nome
        self.__ano = ano
        self.__valor_avaliado = valor_avaliado
        self.posicao_na_lista = " "
        self.nome_da_variavel = " "

    def mostrar_dados_do_veiculo(self):
        return f'\nmontadora = "{self.__montadora}"    \n' \
               f'nome = "{self.__nome}"    \n' \
               f'ano = "{self.__ano}"    \n' \
               f'valor_avaliado = "{self.__valor_avaliado}"    \n'

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
    def valor_avaliado(self):
        return self.__valor_avaliado

    @valor_avaliado.setter
    def preco(self, valor_avaliado):
        self.__valor_avaliado = valor_avaliado

