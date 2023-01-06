from abc import ABC, abstractmethod

from entrada_de_dados.mascarar_preco import mascarar_preco


class Veiculo(ABC):  # Classe Abstrata

    def __init__(self, montadora, nome, ano, valor_de_aquisicao, codigo):
        self.__montadora = montadora
        self.__nome = nome
        self.__ano = ano
        self.__valor_de_aquisicao = valor_de_aquisicao
        self.__codigo = codigo

        self.__cnpj_loja = None

        self.linha_no_arquivo = int()

        self.posicao_na_lista = " "
        self.nome_da_variavel = " "
        self.codigo_de_venda = " "

    def mostrar_atributos_principais(self):
        return f'\nmontadora = "{self.__montadora}"    \n' \
               f'nome = "{self.__nome}"    \n' \
               f'ano = "{self.__ano}"    \n' \
               f'valor_de_aquisicao = "{self.__valor_de_aquisicao}"    \n' \
               f'codigo_de_registro = "{self.__codigo}"    \n'

    def mostrar_dados(self):
        return f'\nmontadora = "{self.__montadora}"    \n' \
               f'nome = "{self.__nome}"    \n' \
               f'ano = "{self.__ano}"    \n' \
               f'valor de aquisicao = "R$:{mascarar_preco(self.__valor_de_aquisicao)}"    \n' \
               f'codigo de registro = "{self.__codigo}"    \n' \
               f'loja = {self.__cnpj_loja}    \n' \

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
    def cnpj_loja(self):
        return self.__cnpj_loja

    @cnpj_loja.setter
    def cnpj_loja(self, cnpj_loja):
        self.__cnpj_loja = cnpj_loja
