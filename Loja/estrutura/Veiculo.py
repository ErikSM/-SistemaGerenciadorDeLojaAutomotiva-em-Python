from abc import ABC, abstractmethod


class Veiculo(ABC):  # Classe Abstrata

    def __init__(self, montadora, nome, ano, valor_avaliado):
        self.__montadora = montadora
        self.__nome = nome
        self.__ano = ano
        self.__valor_avaliado = valor_avaliado
        self.posicao_na_lista = " "

    @abstractmethod
    def abstractmethod(self):
        pass

    def __str__(self):
        return f'\nmontadora = "{self.__montadora}"    \n' \
               f'nome = "{self.__nome}"    \n' \
               f'ano = "{self.__ano}"    \n' \
               f'valor_avaliado = "{self.__valor_avaliado}"    \n'

    def mostrar_sem_pular_linha(self):
        return f'\nMontadora:{self.__montadora}   ' \
               f'Nome:{self.__nome}   ' \
               f'Ano:{self.__ano}   ' \
               f'Avaliado:{self.__valor_avaliado}   '

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

